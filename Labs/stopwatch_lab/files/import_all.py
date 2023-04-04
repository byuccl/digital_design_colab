import os
import requests


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)


def import_text(text):
    url = (
        "https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Labs/seven_segment_lab/files/%s"
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
    import_text("simulation.py")
    import_text("convertData.py")


def import_source():
    cd("/content/tmp_code")
    import_text_bin("TBtemplate.txt")
    import_text("simTemplate.txt")
    import_text_bin("simTemplate2.txt")
    import_text("mod_counter.sv")
    import_text("mod_counter.stm")
    import_text("stopwatch.sv")
    import_text("stopwatch.stm")
    import_text("stopwatch_top.sv")
    import_text("stopwatch_top.stm")
    import_text("SevenSegmentControl.sv")
    cd("/content")
