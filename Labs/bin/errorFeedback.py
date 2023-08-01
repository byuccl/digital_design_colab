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

def search_stderr(err):
    error_start = err.find("ERROR")
    if error_start == -1:
        return err
        
    error_end = err.find("\n", error_start)
    error = err[error_start:error_end]
    return error

def search_stdout_surelog(out):
    error_start = out.find("SNT:")
    if error_start == -1:
        error_start = out.find("ERR:")
        if error_start == -1:
            return ""
    
    error_end = out.find("\n", error_start)
    error = out[error_start+12:error_end]
    return error

def run_main():
    p = subprocess.run(["make", "SURELOG_CMD='-parse'"], capture_output=True)
    err = "".join([str(p.stderr).replace("\\t", "\t").replace("\\n", "\n")
            .replace(r"\'", r"'").replace("\\\\", "\\")[2:-1]]).strip()
    out = "".join([str(p.stdout).replace("\\t", "\t").replace("\\n", "\n")
            .replace(r"\'", r"'").replace("\\\\", "\\")[2:-1]]).strip()

    if err == "":
        print("Your design compiled successfully")
        return

    error = search_stderr(err)
    
    if error == "ERROR: Error when parsing design. Aborting!":
        error = error + "\n" + search_stdout_surelog(out)

    for pattern in errors_dict:
        if re.search(pattern, error) != None:
            print(error)
            print('-'*75)
            print(errors_dict[pattern])
            return
    
    print(error)
    



if __name__ == "__main__":
    run_main()
