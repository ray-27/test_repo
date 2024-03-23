from subprocess import call

def open_file():
    call(["ls"])
    call(["pip", "install", "-r", "requirements.txt"])
    # call(["clear"])

open_file()