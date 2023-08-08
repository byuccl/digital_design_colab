import subprocess
import re

errors_dict = {"ERROR: set_property IO_LOC_PAIRS: Incorrect number of arguments." : "You have a pin in your xdc file that does not match an input or output from your design. Check to see if all the signal names match or if you have too many pins uncommented",
"Syntax error: missing ';' at .*" : "You are missing a semicolon. It needs to go right before the line number mentioned above",
"Syntax error: extraneous input '<EOF>' expecting {" : "You are missing \"endmodule\" at the end of your file",
"Syntax error: mismatched input .* expecting <EOF>" : "You have \"endmodule\" appearing too early in your design. Some operations like \"assign\" and \"defparam\" can't be peformed after \"endmodule\"",
"Syntax error: extraneous input '(?!<EOF>$).*' expecting {" : "Make sure you have an \"end\" for every \"begin\" in your code. It can be easy to miss one especially if you have many statements nested",
"Syntax error: rule conditional_statement failed predicate:" : "You have a syntax error in your if/else statement",
"ERROR: Module .* referenced in module .* is not part of the design." : "You misspelled your module instantiation",
"ERROR: Module .* not found!" : "You may have mispelled the top module name in the makefile",
r"ERROR: Latch inferred for signal `\\.*`\\" : "The compiler inferred sequential logic in an always_comb block. This is because you don't have a default value for each signal. Make sure that every signal is assigned a value for each if/else case. Or put the default value for all signals at the top of the always comb block",
"ERROR: .* expression of procedural for-loop is not" : "You have a problem in your for loop. Make sure the variable used is of type \"integer\". It might help to declare it outside of the for loop",
"Illegal lhs of type " : "The signal used on the left hand side of the expression is not valid. It may be of the wrong type, or it may be misspelled so the wrong type is inferred",
"Undefined type \".*\"\." : "The type you used to declare the signal is invalid. It may be misspelled",
"make: \*\*\* No rule to make target .*" : "You have an error in your Makefile. You may have the wrong source or xdc files listed, or the wrong path to common.mk",
"make: \*\*\* No targets specified and no makefile found.  Stop." : """
You do not have a makefile. Create one by following this template:

current_dir := ${CURDIR}
TARGET := basys3

TOP := myTopMOdule

XDC := ${current_dir}/*.xdc

SOURCES := $(wildcard ${current_dir}/*.v ${current_dir}/*.sv)

include ${F4PGA_EXAMPLES_ROOT}/f4pga-examples/common/common.mk
"""
}

def print_compiled_info(out):
    warnings = re.findall(r"\[WRN:.*\n", out)
    print("Your design compiled successfully with {} warning{}:".format(len(warnings), ("" if len(warnings) == 1 else "s")))
    print()
    for warn in warnings:
        print(warn)
    print('-'*75)
    print("Design Statistics:\n")
    design_stats_beg = out.find("Number of wires")
    design_stats_end = out.find("38. Executing ATTRMAP pass (move or copy attributes).")
    print(out[design_stats_beg-3:design_stats_end-1])
    print('-'*75)
    print("Circuit Statistics")
    circuit_stats_beg = out.find("Circuit Statistics:")
    circuit_stats_end = out.find("Build Timing Graph\n")
    print(out[circuit_stats_beg+19:circuit_stats_end])
    print('-'*75)
    utilization_beg = out.find("Device Utilization:")
    utilization_end = out.find("# Build Device Grid took")
    utilization = out[utilization_beg:utilization_end]
    utilization = utilization.splitlines()
    section = []
    for line in utilization:
        if line.find("Device Utilization:") != -1:
            print(line)
            print()
        elif line.find("Physical Tile") != -1:
            if len(section) > 1:
                for sentence in section:
                    print(sentence)
            section = []
            section.append(line)
        else:
            if line.find("0.00") == -1:
                section.append(line)
    for sentence in section:
        print(sentence)

def search_stderr(err):
    error_start = err.find("ERROR")
    if error_start == -1:
        return err
        
    error_end = err.find("\n", error_start)
    error = err[error_start:error_end]
    return error

def search_parse_error(out):
    error_start = out.find("SNT:")
    if error_start == -1:
        error_start = out.find("ERR:")
        if error_start == -1:
            return ""
    
    error_end = out.find("\n", error_start)
    error = out[error_start+12:error_end]
    return error

def search_tcl_error(out):
    error_start = out.find("ERROR:")
    if error_start == -1:
        return ""
    
    error_end = out.find("\n", error_start)
    error = out[error_start:error_end]
    return error

def run_main():
    with open('error.txt', 'r') as f:
        lines = f.readlines()
        err = ''.join(lines)
    with open('compile.txt', 'r') as f:
            lines = f.readlines()
            out = ''.join(lines)
    
    if err == "":
        print_compiled_info(out)
        return

    error = search_stderr(err)
    
    if error == "ERROR: Error when parsing design. Aborting!":
        error = error + "\n" + search_parse_error(out)

    if error == "ERROR: TCL interpreter returned an error: Yosys command produced an error":
        error = error + "\n" + search_tcl_error(out)


    for pattern in errors_dict:
        if re.search(pattern, error) != None:
            print(error)
            print('-'*75)
            print(errors_dict[pattern])
            return
    
    print(error)

if __name__ == "__main__":
    run_main()
