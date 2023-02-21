import os


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)
    # print("##### Changing to " + os.getcwd() + "#####")


def import_text(text):
    url = "https://raw.githubusercontent.com/westonMS/tempColab/main/Labs/bin/%s" % text
    resp = requests.get(url)
    with open(text, "wb") as f:
        f.write(resp.content)


def import_all():
    cd("/content/tmp_code")
    import_text("TBtemplate.txt")
    import_text("simTemplate.txt")
    import_text("simTemplate2.txt")
    import_text("function1.sv")
    import_text("function1.stm")
    import_text("function2.sv")
    import_text("function2.stm")
    import_text("function3.sv")
    import_text("function3.stm")
    import_text("function4.sv")
    import_text("function4.stm")
    import_text("dataflow_sv.stm")
    import_text("dataflow_sv.sv")
    import_text("tb_function1.cpp")
    import_text("tb_function2.cpp")
    import_text("tb_function3.cpp")
    import_text("tb_function4.cpp")
