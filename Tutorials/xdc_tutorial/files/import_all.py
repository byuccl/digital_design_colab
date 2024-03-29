import os
import requests


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)


def import_text(text):
    url = (
        "https://raw.githubusercontent.com/byuccl/digital_design_colab2/master/Labs/xdc_lab/files/%s"
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
    cd("/content")
