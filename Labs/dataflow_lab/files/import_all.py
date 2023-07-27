import os
import requests


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)


def import_text(text):
    url = (
        "https://raw.githubusercontent.com/byuccl/digital_design_colab/master/Labs/dataflow_lab/files/%s"
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
    import_text("function1.sv")
    import_text("function1.stm")
    import_text("function2.sv")
    import_text("function2.stm")
    import_text("function3.sv")
    import_text("function3.stm")
    import_text("function4.sv")
    import_text("function4.stm")
    import_text("dataflow.sv")
    import_text("dataflow.stm")
    import_text("tb_function1.cpp")
    import_text("tb_function2.cpp")
    import_text("tb_function3.cpp")
    import_text("tb_function4.cpp")
    import_text("tb_dataflow.cpp")
    cd("/content")
