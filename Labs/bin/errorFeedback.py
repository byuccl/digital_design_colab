import subprocess

errors_dict = {"ERROR: set_property IO_LOC_PAIRS: Incorrect number of arguments." : "You have a pin in your xdc file that does not match an input or output from your design. Check to see if all the signal names match or if you have too many pins uncommented",
"ERROR: syntax error, unexpected TOK_ASSIGN" : "You have a syntax error. You are probably missing a semicolon",
"ERROR: syntax error, unexpected TOK_ENDMODULE" : "Something is wrong around 'endmodule' in .sv your design file. Maybe you are missing a semicolon before it. Maybe you forgot to end a block.",
"ERROR: syntax error, unexpected end of file" : "You are missing 'endmodule' and the end of .sv your design file",
"ERROR: Error when parsing design. Aborting!" : "",
"Message: Clock name or pattern '\$iopadmap\$clk' does not correspond to any nets. To create a virtual clock, use the '-name' option." : "You mistyped a signal name in your .sv design file"
}

def search_stderr(err):
    error_start = err.find("ERROR")
    if error_start == -1:
        return ""
        
    error_end = err.find("\n", error_start)
    error = err[error_start:error_end]
    return error

def search_stdout_yosys(out):
    error_start = out.find("Message")
    if error_start == -1:
        return ""

    error_end = out.find("\n", error_start)
    error = out[error_start:error_end]
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
    if error == "" or error == "ERROR: Error when parsing design. Aborting!":
        error = error + "\n" + search_stdout_surelog(out)

    if error in errors_dict:
        print(error)
        print(errors_dict[error])
    else:
        print(error)


if __name__ == "__main__":
    run_main()