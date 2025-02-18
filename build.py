from cx_Freeze import setup, Executable

setup(
    name="karfagen",
    version="0.1",
    description="Karfagen - open src fb2 reader",
    executables=[
        Executable(
            "reader.pyw",
            icon="./media/karfagen.ico",
            base="Win32GUI"
        )
    ],
    base="Win32GUI",
)
