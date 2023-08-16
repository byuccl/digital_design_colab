import os
import requests


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)


def import_text(text):
    url = (
        "https://raw.githubusercontent.com/resoluteprogrammer/digital_design_colab/master/Labs/seven_segment_lab/files/%s"
        % text
    )
    resp = requests.get(url)
    with open(text, "wb") as f:
        f.write(resp.content)

def import_from_bin(text):
    url = (
        "https://raw.githubusercontent.com/resoluteprogrammer/digital_design_colab/master/Labs/bin/%s"
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
    import_text("seven_segment.sv")
    import_text("seven_segment.stm")
    import_text("seven_segment_top.sv")
    import_text("seven_segment_top.stm")
    import_text("tb_seven_segment.cpp")
    cd("/content")
