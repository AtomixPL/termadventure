import sys
import os
import subprocess

def is_powershell():
    return 'PSModulePath' in os.environ

def installdeps():
    print("Setting up virtual environment...")
    subprocess.run([sys.executable,"-m","venv","venv"],text=True,check=True)
    if sys.platform=="win32":
        venv_python = os.path.join("venv","Scripts","python.exe")
    else:
        venv_python = "./"+os.path.join("venv","bin","python")
    print("Installing colorama and PyInstaller modules...")
    subprocess.run([venv_python,"-m","pip","install","colorama","pyinstaller"],text=True,check=True)

def build():
    print("Building executable...")
    if sys.platform=="win32":
        subprocess.run([sys.executable,"-m","PyInstaller","-F","src/termadventure.py"],text=True,check=True)
    elif sys.platform=="linux":
        subprocess.run(["./venv/bin/python","-m","PyInstaller","-F","src/termadventure.py"],text=True,check=True)
    print("Cleaning up...")
    if sys.platform=="win32":
        if is_powershell():
            subprocess.run(["powershell.exe", "-Command", "Remove-Item","-Recurse","build"],text=True,check=True)
            subprocess.run(["powershell.exe", "-Command", "Remove-Item","termadventure.spec"],text=True,check=True)
        else:
            subprocess.run(["rd", "/s", "/q", "build"], check=True)
            subprocess.run(["del","termadventure.spec"], check=True)
    elif sys.platform=="linux":
        subprocess.run(["rm","-rf","build"],text=True,check=True)
        subprocess.run(["rm","termadventure.spec"],text=True,check=True)
        
if __name__ == "__main__":
    installdeps()
    build()
    print("Setup finished")