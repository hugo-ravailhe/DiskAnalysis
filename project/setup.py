from cx_Freeze import setup, Executable

setup(
    name="Disk Analysis",
    version="0.1",
    description="Logiciel pour analysé la tailles des données sur son pc",
    executables=[Executable("program.py")]
)