from cx_Freeze import setup, Executable

setup(
    name = "karfagen",
    version = "0.1",
    description = "Karfagen - open source fb2 reader",
    executables = [Executable("reader.py")],
    base="Win32GUI",

)
