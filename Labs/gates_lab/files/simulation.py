# @title Anon Simulation Widget { form-width: "50px" }
import os
import re
import sys
import subprocess
from collections import defaultdict, namedtuple
import subprocess
import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider
from google.colab import drive


VerilogIO = namedtuple("VerilogIO", "dir nam wid")
"""
        Using a namedtuple (sort of like a C-struct) to hold info on each Verilog IO.
        This is very similar to using a class with only data members.
          The advantages are: (1) the fields are not change-able after creation
          (which is what I want), and (2) probably more efficient than using a class.
        This is used by both generate() and processVmoduleHFile() so it is declared in global scope.
"""


def vcd():
    x = subprocess.run(
        ["cat", "/content/tmp_code/logs/vlt_dump.vcd"], check=True, capture_output=True
    )
    y = subprocess.run(["vcd"], input=x.stdout, capture_output=True)
    z = y.stdout.decode("utf-8").strip()
    z = z.split("\n")[10:]
    a = ""
    for i in z:
        a += i + "\n"
    print(a)


def getModuleName(textSourceCode):
    match_name = re.search(
        r"module\s{1,}\w{1,}\s{0,}#{0,}\s{0,}\(", textSourceCode.value
    )
    if match_name is None:
        return None
    mname = match_name.group().split(" ")[1]
    mname = mname.split("(")[0]
    mname = mname.split("#")[0]
    return mname


def writeJson(d, fname="/tmp/json.json", ind=2):
    """Write an object to a file with indenting"""
    import json

    with open(fname, encoding="utf-8", mode="w") as f:
        json.dump(d, f, indent=ind)


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)
    # print("##### Changing to " + os.getcwd() + "#####")


def getNextLine(f):
    """Read file f until you get a non-comment and a non-blank link.
    The returned line will be stripped of whitespace (including newline)
    """
    while True:
        myLine = f.readline().strip()
        if not myLine.startswith("//") and len(myLine) > 0:
            break
    return myLine


def processSTMHeader(tBench):
    """
    Read STM file and pull out the clock definition and the list of inputs.
    Note that for combinational circuits we are expecting a clock line
      consisting of 'comb' (which is ignored)
    """
    with open(tBench, encoding="utf-8", mode="r") as f:
        stmClock = None
        tmp = getNextLine(f)
        if tmp != "comb":
            stmClock = tmp
        inputs = getNextLine(f).split()

    # Verify that a signal doesn't appear twice in the list (this is a user-created file after all)
    for elmt in inputs:
        assert (
            inputs.count(elmt) == 1
        ), "Cannot have duplicate names in STM file input list. ({} appears more than once)".format(
            elmt
        )
    return (stmClock, inputs)


def processVmoduleHFile(fname, stmClock, stmInputs):
    """
    Process the verilator-produced Vmodule.h file and pull out
    the IO definitions.  Pack them into the verilogIOs structure,
    which is a list of lists consisting of [dir, name, size].
    Along the way see if you can match any of the signals as
    corresponding to the clock defined in the stimulus file.
    Finally, make sure that all verilog signals are in the stm file
      and the other way around.
    """

    verilogIOs = []
    with open(fname, encoding="utf-8", mode="r") as f:
        verilogClock = None
        for line in f:
            line = line.strip()
            if line.startswith(
                "// LOCAL VARIABLES"
            ):  # Can skip everything after this line
                break
            match = re.match(r"^VL_(IN|OUT|SIG)(\d*)\(([^,]*),(\d+),(\d+)", line)
            if match is not None:
                varDir, varName, varSize = [
                    match.groups()[0],
                    match.groups()[2],
                    int(match.groups()[3]) - int(match.groups()[4]) + 1,
                ]
                verilogIOs.append(VerilogIO(varDir, varName, varSize))
                # If input, check that it is in STM file
                if varName == stmClock:
                    verilogClock = varName  # Found matching clock names between STM and Verilog header

    # Check to make sure that every stm input is in the verilog file
    #   and the other way around.
    for si in stmInputs:
        assert si in [
            f.nam for f in verilogIOs if f.dir == "IN"
        ], "ERROR: input '{}' in STM file but not in Verilog design".format(si)
    for vi in [f.nam for f in verilogIOs if f.dir == "IN"]:
        assert (
            vi == stmClock or vi in stmInputs
        ), "ERROR: input '{}' in Verilog design but not in STM file".format(vi)

    # Make sure that if a clock was in the STM file, it was found in the Verilog
    if stmClock != None:
        assert (
            verilogClock != None
        ), "There was a clock defined in the STM file but no corresponding clock in the Verilog file."
    return (verilogClock, verilogIOs)


from string import Template


def generate(
    designFolder,
    verilogFile,
    tBenchFile,
    draw=True,
    wall=True,
    compress=True,
    Hex=True,
    verbose=False,
    pythonPath="",
    processClockWaveform=True,
    hscale=1,
    nameOrder="",
):
    """
    Generate a C++ object of verilog/systemverilog code using verilator, toggle inputs on said C++ object,
    and portray resulting waveforms of the signals. Comments in the stm file are supported and are indicated with //
    Comments must start at the beginning of the line and are expected to take up the whole line
    Keyword Arguements:
    designFolder -- str - relative path of the directory, where the .v and .stm files are
    verilogFile -- str - the top level HDL module
    tBenchFile -- str - the name of a .stm file of input stimulus.
    draw -- bool - whether or not to display the waveform
    wall -- bool whether or not to check for verilator warnings
    compress -- bool whether or not to compress the c++ object made by verilator. (Compression effectively
      eliminates the ability to view most internal signals  (deprecated)
    Hex -- bool - whether to display waveform values in hexadecimal
    verbose -- bool - control verbose mode
    pythonPath -- str - path to directory where MaverickSimulator project can be found. If left empty, the typical
                        PYTHONPATH/site-packages will be assumed
    processClockWaveform -- bool -  By default, will attempt to convert the clock waveform to one with arrows.
                                    Setting this to False will prevent this
    hscale -- int - Will adjust the width of the ticks on the waveform diagram. This arguement is passed directly
                    to executeSimulation()
    """
    clock = None  # The name of the clock to the design (if any)
    homeDir = os.getcwd()
    try:
        fileNameRoot = os.path.splitext(verilogFile)[0]
        if not pythonPath:
            dirs = sys.path
            for dir in dirs:
                if dir.find("site-packages") != -1:
                    # TODO add check to make sure path is valid
                    pythonPath = dir + "/MaverickSimulator/src"
                    break
        # Adjust commandline args for verilator
        w = " -Wall" if wall else " "
        c = " " if compress else " --public "
        wv = " --trace " if draw else "--trace"

        cd(designFolder)

        # Step 1: run the verilator program
        v = subprocess.Popen(
            r"verilator -cc"
            + w
            + c
            + wv
            + verilogFile
            + " -CFLAGS '-std=c++11' --exe sim___.cpp",  # create verilator object and link to .cpp
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            universal_newlines=True,
        )
        x = v.stdout.read()
        if x.find("Error") != -1:
            raise Exception(x)

        verbose = 0
        if verbose:
            print("Running verilator...")
            print(
                "verilator -cc"
                + w
                + c
                + wv
                + verilogFile
                + " -CFLAGS '-std=c++11' --exe sim___.cpp"
            )
            output = v.stdout.read().strip()
            if len(output) > 0:
                print("Results of running verilator: " + output)
            if output.find("%Error: Command Failed") != -1:
                return 1
                sys.exit("Exiting due to verilator errors")
        else:
            output = v.stdout.read().strip()
            if output.find("%Error: Command Failed") != -1:
                print(output)
                os.chdir(homeDir)
                return 1
                sys.exit("Exiting due to verilator errors")

        # Step 2: Parse STM and Verilog files
        # Open .stm file and get clock and list of inputs from the  first two uncommented lines
        stmClock, stmInputs = processSTMHeader(tBenchFile)

        # Read the IO definitions from the Vmodule.h file
        # Add inputs, outputs, and local signals to data structure verilogIOs
        verilogClock, verilogIOs = processVmoduleHFile(
            "obj_dir/V" + fileNameRoot + ".h", stmClock, stmInputs
        )

        # If verilogClock has been set that means
        # it matched up with the one from the STM file. Otherwise, it did not.
        # The rest of the code will use clock to know this.
        if verilogClock != None:
            clock = verilogClock

        # Step 3:Write the Testbench__lh file
        ios = ""
        sg = ""
        # Build list of IO print stmts for printIOs()
        for nam, wid in [(f.nam, f.wid) for f in verilogIOs if f.dir != "SIG"]:
            print(str(nam) + str(wid))
            ios += '    std::cout << " {0} is " << std::bitset<{1}>(top->{0}) <<  std::endl;\n'.format(
                nam, wid
            )
        print(ios)
        # If needed, build list of IO print stmts for printInternalOs()
        if not compress:
            for nam, wid in [(f.nam, f.wid) for f in verilogIOs if f.dir == "SIG"]:
                varName = nam.replace("v__DOT__", "").replace("__DOT__", " ")
                sg += '   std::cout << "{} is " << std::bitset<{}>(top->{}) << std::endl;\n'.format(
                    varName, wid, nam
                )
        # Now actually write the testBench file into the design directory
        with open(
            "TestBench___.h", encoding="utf-8", mode="w"
        ) as tb:  # header file for interacting with verilator object
            with open("/content/tmp_code/TBtemplate.txt", "r") as tbTemplate:
                t = Template(tbTemplate.read())
                t = t.substitute(
                    MODULE=fileNameRoot,
                    CLKDEF="\n#define CLK top->" + clock if clock else "",
                    IOPRINTS=ios,
                    INTERNALIOPRINTS=sg,
                )
                tb.write(t)

        # Step 4: write the main simulation file
        # Collect IO print code snippets (using simTemplate2.txt as pattern)
        ios = ""
        for inputName in stmInputs:
            for inputWidth in [f.wid for f in verilogIOs if f.nam == inputName]:
                with open("/content/tmp_code/simTemplate2.txt", "r") as simTemplate2:
                    t = Template(simTemplate2.read())
                    t = t.substitute(SIGNAME=inputName, SIGWIDTH=inputWidth)
                    ios += t

        # Now write the main simulation file for compilation (using simTemplate.txt as pattern)
        with open("sim___.cpp", encoding="utf-8", mode="w") as sim:
            with open(
                "/content/tmp_code/simTemplate.txt", encoding="utf-8", mode="r"
            ) as simTemplate:  # now write main.cpp file
                t = Template(simTemplate.read())
                t = t.substitute(
                    NUMINS=len(stmInputs),
                    READINPUTSCODE=ios,
                    HASCLOCK=(0 if clock is None else 1),
                )
                sim.write(t)

        # Step 5: Compile the resulting program
        print("Compiling")
        if verbose:
            print(
                "make -C obj_dir -j -f V"
                + fileNameRoot
                + ".mk V"
                + fileNameRoot
                + "; cd obj_dir"
            )
            v = subprocess.Popen(
                r"make -C obj_dir -j -f V"
                + fileNameRoot
                + ".mk V"
                + fileNameRoot
                + "; cd obj_dir",
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
                universal_newlines=True,
            )
            output = v.stdout.read().strip()
            if len(output) > 0:
                print("   Results of compiling: " + output)
        else:
            v = subprocess.Popen(
                r"make -C obj_dir -j -f V"
                + fileNameRoot
                + ".mk V"
                + fileNameRoot
                + "; cd /content/tmp_code/obj_dir",  # call makefile to g++ compile appropriate files
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
                universal_newlines=True,
            )

        output = v.stdout.read().strip()
        # Step 6: Execute it
        # if not nameOrder:
        #   names = [f.nam for f in verilogIOs if f.dir != 'SIG']
        #   writeJson(names, fname=fileNameRoot+'.nmo')
        #   nameOrder = fileNameRoot+'.nmo'
        # cd(homeDir)
        # ret = executeSimulation(designFolder, verilogFile, tBenchFile, draw,
        #                     compress, Hex, verbose, clock, nameOrder,
        #                     processClockWaveform, hscale, pythonPath)
        # if draw is False:
        #     return ret
        0
        subprocess.run(
            [
                "/content/tmp_code/obj_dir/V" + fileNameRoot,
                "/content/tmp_code" + fileNameRoot + ".stm",
                "--trace",
            ]
        )
        # !./tmp_code/obj_dir/VbehavLoadableReg /content/tmp_code/temp.stm --trace
        # !vcd < /content/logs/vlt_dump.vcd
        subprocess.run(["vcd", "<", "/content/logs/vlt_dump.vcd"])
    except Exception as e:
        os.chdir(homeDir)
        print(str(e))
        raise e


def showWaveformClicked(self):
    sc = cellDict[self]
    assert sc is not None, "Internal error with cellDict"

    if (
        submitCodes(
            sc.interpreterHomeDir,
            sc.textSourceCode,
            sc.textStimulus,
            sc.selectHexBin.value,
        )
        == False
    ):
        return
    srcFileName = getModuleName(sc.textSourceCode)
    arrow = sc.chkArrow.value
    hex = True if sc.selectHexBin.value == "Hex" else False
    assert os.path.exists(
        sc.interpreterHomeDir + "/tmp_code/" + srcFileName + ".sv"
    ), "Please submit the codes before showing waveform: {} {}".format(
        sc.interpreterHomeDir, srcFileName
    )

    try:
        generate(
            sc.interpreterHomeDir + "/tmp_code",
            srcFileName + ".sv",
            srcFileName + ".stm",
            compress=True,
            Hex=hex,
            verbose=True,
            processClockWaveform=arrow,
        )
    except Exception as e:
        return

    print(
        "###########################################################################################"
    )
    x = subprocess.run(
        [
            "/content/tmp_code/obj_dir/V" + srcFileName,
            "/content/tmp_code/" + srcFileName + ".stm",
            "--trace",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    print(x.stderr + x.stdout)
    vcd()

    if sc.showCode.value:
        print(
            "------------------------------------------------------------------------------------------"
        )
        print("Source code for the simulation above:")
        print(
            "------------------------------------------------------------------------------------------"
        )
        print(sc.textSourceCode.value)
        print(
            "------------------------------------------------------------------------------------------"
        )


class SimCell:
    def __init__(
        self,
        textSourceCode,
        textStimulus,
        chkArrow,
        selectHexBin,
        interpreterHomeDir,
        showCode,
        contents,
    ):
        self.textSourceCode = textSourceCode
        self.textStimulus = textStimulus
        self.chkArrow = chkArrow
        self.selectHexBin = selectHexBin
        self.interpreterHomeDir = "/content"
        self.showCode = showCode
        self.contents = contents


def readContents(contents):
    if contents is None:
        code = ""
        stim = ""
    else:
        print(contents)
        contents = "/content/" + contents
        with open(contents + ".sv") as f:
            code = f.read()
        with open(contents + ".stm") as f:
            stim = f.read()
        # with open(JTEXT+'/pgms/' + contents[:-1] + "tm") as f:
        #     stim = f.read()
    return [code, stim]


cellDict = dict()


def CreateWidgets(contents, ht="125px", wid="500px", stht="125px", stwid="500px"):
    code, stim = readContents(contents)

    srcCodeWidget = widgets.Textarea(
        disabled=False,
        value=code,
        layout=widgets.Layout(height=ht, width=wid),
    )

    stimulusWidget = widgets.Textarea(
        value=stim,
        disabled=False,
        layout=widgets.Layout(height=stht, width=stwid),
    )

    selectHexBin = widgets.Dropdown(
        options=["Binary", "Hex", "Decimal"],
        value="Decimal",
        description="",
        disabled=False,
    )

    chkArrow = widgets.Checkbox(
        description="Show the clock arrow", value=True, indent=False
    )
    showCode = widgets.Checkbox(
        description="Show source code below waveform", value=False, indent=False
    )
    # butt_submit = widgets.Button(description='Save code')
    butt_show_waveform = widgets.Button(description="Run simulation", layout=Layout(width="300px", border='solid 1px gray'))
    butt_refresh_contents = widgets.Button(description="Restore code", layout=Layout(border='solid 1px gray'))
    butt_save_code = widgets.Button(description="Save code", layout=Layout(border='solid 1px gray'))
    butt_save_drive_code = widgets.Button(description="Save code to Drive", layout=Layout(border='solid 1px gray'))
    butt_load_drive_code = widgets.Button(description="Load code from Drive", layout=Layout(border='solid 1px gray'))
    return (
        srcCodeWidget,
        stimulusWidget,
        selectHexBin,
        chkArrow,
        showCode,
        butt_show_waveform,
        butt_refresh_contents,
        butt_save_code,
        butt_save_drive_code,
        butt_load_drive_code
    )


def submitCodes(interpreterHomeDir, textSourceCode, textStimulus, selectHexBin):
    print(selectHexBin)
    if textSourceCode.value == "" or textStimulus.value == "":
        print("The source code and stimulus cannot be empty! Please input again")
        print(
            "###########################################################################################"
        )
        return False
    else:
        with open(
            interpreterHomeDir + "/tmp_code/" + getModuleName(textSourceCode) + ".sv",
            "w",
        ) as f:
            f.write(textSourceCode.value)
        with open(
            interpreterHomeDir + "/tmp_code/" + getModuleName(textSourceCode) + ".stm",
            "w",
        ) as f:
            temp_string = textStimulus.value
            temp_string = temp_string + "\n" + "\n"
            skip_two_lines = 0
            cur_substring = ""
            last_break = ""
            binary = ["0", "1", "\n", " "]
            hex = [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                " ",
                "\n",
            ]
            if selectHexBin == "Hex":
                for i in textStimulus.value:
                    if i == "\n" and skip_two_lines != 2:
                        skip_two_lines += 1
                        last_break = "\n"
                        continue
                    if skip_two_lines < 2:
                        continue
                    if hex.count(i) == 0:
                        print("Invalid Hex Character, Removing...")
                        temp_string = temp_string.replace(i, "")
                        continue
                    if i != " " and i != "\n":
                        cur_substring = cur_substring + i
                    elif i == " " and cur_substring:
                        temp_string = temp_string.replace(
                            last_break + cur_substring + i,
                            last_break + str(int(cur_substring, 16)) + " ",
                        )
                        last_break = " "
                        cur_substring = ""
                    elif i == "\n" and cur_substring:
                        temp_string = temp_string.replace(
                            last_break + cur_substring + i,
                            last_break + str(int(cur_substring, 16)) + "\n",
                        )
                        last_break = "\n"
                        cur_substring = ""
                    elif i == " ":
                        last_break = " "
                    elif i == "\n":
                        last_break = "\n"
            elif selectHexBin == "Binary":
                for i in textStimulus.value:
                    if i == "\n" and skip_two_lines != 2:
                        skip_two_lines += 1
                        last_break = "\n"
                        continue
                    if skip_two_lines < 2:
                        continue
                    if binary.count(i) == 0:
                        print("Invalid Hex Character, Skipping...")
                        continue
                    if i != " " and i != "\n":
                        cur_substring = cur_substring + i
                    elif i == " " and cur_substring:
                        temp_string = temp_string.replace(
                            last_break + cur_substring + i,
                            last_break + str(int(cur_substring, 2)) + " ",
                        )
                        last_break = " "
                        cur_substring = ""
                    elif i == "\n" and cur_substring:
                        temp_string = temp_string.replace(
                            last_break + cur_substring + i,
                            last_break + str(int(cur_substring, 2)) + "\n",
                        )
                        last_break = "\n"
                        cur_substring = ""
                    elif i == " ":
                        last_break = " "
                    elif i == "\n":
                        last_break = "\n"
            if selectHexBin != "Decimal":
                print(f"Converted Values of STM \n")
                print(temp_string)
            f.write(temp_string[:-1])
    return True


def refreshContentsClicked(self):
    sc = cellDict[self]
    assert sc is not None, "Internal error with cellDict"
    code, stim = readContents(sc.contents)
    sc.textSourceCode.value = code
    sc.textStimulus.value = stim

def readFromDriveClicked(self):
    sc = cellDict[self]
    assert sc is not None, "Internal error with cellDict"
    drive.mount('/content/drive')
    code, stim = readContents("drive/MyDrive/test/"+sc.contents)
    sc.textSourceCode.value = code
    sc.textStimulus.value = stim
    drive.flush_and_unmount()


def overwriteSavedCode(self):
    sc = cellDict[self]
    print(sc.contents)
    file_location = "/content/" + sc.contents
    with open(file_location + ".sv", "w") as f:
        f.write(sc.textSourceCode.value)
    with open(file_location + ".stm", "w") as f:
        f.write(sc.textStimulus.value)

def saveToDrive(self):
    sc = cellDict[self]
    print(sc.contents)
    drive.mount('/content/drive')
    file_location = "/content/drive/MyDrive/test/" + sc.contents
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location + ".sv", "w") as f:
        f.write(sc.textSourceCode.value)
    with open(file_location + ".stm", "w") as f:
        f.write(sc.textStimulus.value)
    drive.flush_and_unmount()


def createSimulationWorkSpace(
    initialContents=None, ht="500px", wid="920px", stht="300px", stwid="600px"
):
    interpreterHomeDir = os.getcwd()
    code_file_path = interpreterHomeDir + "/tmp_code"
    if not os.path.exists(code_file_path):
        os.mkdir(code_file_path)

    # Create widgets for this part
    (
        textSourceCode,
        textStimulus,
        selectHexBin,
        chkArrow,
        showCode,
        btnShowWaveform,
        btnRestoreCode,
        btnSaveCode,
        btnSaveToDrive,
        btnRestoreFromDrive,
    ) = CreateWidgets(initialContents, ht, wid, stht, stwid)
    # print(textSourceCode.value)
    # print(textStimulus.value)

    # Register callbacks for when clicking the button
    btnShowWaveform.on_click(showWaveformClicked)
    btnRestoreCode.on_click(refreshContentsClicked)
    btnSaveCode.on_click(overwriteSavedCode)
    btnSaveToDrive.on_click(saveToDrive)
    btnRestoreFromDrive.on_click(readFromDriveClicked)
    # Register this cell's info
    sc = SimCell(
        textSourceCode,
        textStimulus,
        chkArrow,
        selectHexBin,
        interpreterHomeDir,
        showCode,
        initialContents,
    )
    cellDict[btnShowWaveform] = sc
    cellDict[btnRestoreCode] = sc
    cellDict[btnSaveCode] = sc
    cellDict[btnSaveToDrive] = sc
    cellDict[btnRestoreFromDrive] = sc

    # Draw cell widgets
    topPart = widgets.HBox([
        widgets.VBox([widgets.Label("Source code area:"), textSourceCode])
    ])
    bottomPart = widgets.HBox(
        [
            widgets.VBox([widgets.Label("Simulation code area:"), textStimulus]),
            widgets.Label(""),widgets.Label(""),widgets.Label(""),widgets.Label(""),
            widgets.VBox([
                widgets.Label(""),
                widgets.HBox([btnSaveCode,btnRestoreCode]),
                widgets.HBox([btnSaveToDrive,btnRestoreFromDrive]),
                widgets.Label(""),
                widgets.Label("Select Simulation Input Type"),
                selectHexBin,
                showCode,
                btnShowWaveform,
            ])
        ]
    )

    # Show widgets
    display(widgets.VBox([topPart, bottomPart]))
