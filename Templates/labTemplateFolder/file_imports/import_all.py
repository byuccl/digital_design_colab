#This file is used to import and do the following
#Imports Required Modules: It imports the os and requests modules to interact with the operating system and make HTTP requests, respectively.
#
#Defines Utility Functions:
#    cd(folder): A wrapper for the os.chdir() function that changes the current working directory to the specified folder.
#   import_text(text): Downloads a text file from a predefined URL and saves it locally. The URL is formatted to include the filename specified by the text parameter.
#   import_from_bin(text): Similar to import_text, but intended for binary files. It downloads a file from another predefined URL, also formatted with the text parameter, and saves it locally.
#
#Defines Main Functionality:
#   import_all(): A function that calls two other functions, import_packages() and import_source(), to import all required packages and source files.
#   import_packages(): Changes the directory to /content, then imports several binary files (simulation.py, vcd2wd.py) by calling import_from_bin with the file names.
#   import_source(): Changes the directory to /content/tmp_code, then imports a mix of binary and text files related to what seems like a digital design or simulation project. These files include various .sv (SystemVerilog files), .stm (probably stimulus files for simulations), and .cpp (C++ files) for test benches. After importing these files, it changes the directory back to /content.'''



import os
import requests


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)


def import_text(text):
    url = (
        "https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/stopwatch_lab/files/%s"
        % text
    )
    resp = requests.get(url)
    with open(text, "wb") as f:
        f.write(resp.content)

def import_from_bin(text):
    url = (
        "https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/bin/%s"
        % text
    )
    resp = requests.get(url)
    with open(text, "wb") as f:
        f.write(resp.content)

def import_all():
    import_packages()
    import_source()

def import_packages():
    cd("/content")
    import_from_bin("simulation.py")
    import_from_bin("vcd2wd.py")

def import_source():
    cd("/content/tmp_code")
    import_from_bin("errorFeedback.py")
    import_from_bin("TBtemplate.txt")
    import_from_bin("simTemplate.txt")
    import_from_bin("simTemplate2.txt")
    import_text("mod_counter.sv")
    import_text("mod_counter.stm")
    import_text("stopwatch.sv")
    import_text("stopwatch.stm")
    import_text("stopwatch_top.sv")
    import_text("stopwatch_top.stm")
    import_text("SevenSegmentControl.sv")
    import_text("config.vlt")
    cd("/content")
