import os
import requests


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)


def import_text(text):
    url = (
        "https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Labs/dataflow_lab/files/%s"
        % text
    )
    resp = requests.get(url)
    with open(text, "wb") as f:
        f.write(resp.content)


def import_packages():
    cd("/content")
    import_text("simulation.py")
    import_text("convertData.py")


def import_source():
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
    import_text("dataflow.sv")
    import_text("dataflow.stm")
    import_text("tb_function1.cpp")
    import_text("tb_function2.cpp")
    import_text("tb_function3.cpp")
    import_text("tb_function4.cpp")
    import_text("tb_dataflow.cpp")
    cd("/content")
