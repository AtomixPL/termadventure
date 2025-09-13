import subprocess
import os
import sys

def create_venv():
    if not os.path.exists(".venv"):
        print("Creating virtual environment...")
        if os.name == 'nt':
            subprocess.run(["cmd.exe", "/c", "python -m venv .venv && .venv\\Scripts\\activate"], check=True)
        elif os.name == 'posix':
            subprocess.run(["/bin/bash", "-c", "python3 -m venv .venv && source .venv/bin/activate && .venv/bin/pip install --upgrade pip colorama pyinstaller"], check=True)
        else:
            print("Unsupported OS for virtual environment creation.")
            exit(1)
    else:
        print("Virtual environment already exists.")

def remove_venv():
    if os.path.exists(".venv"):
        print("Removing virtual environment...")
        if os.name == 'nt':
            subprocess.run(["cmd.exe", "/c", "rmdir /s /q .venv"], check=True)
        elif os.name == 'posix':
            subprocess.run(["/bin/bash", "-c", "rm -rf .venv"], check=True)
        else:
            print("Unsupported OS for virtual environment removal.")
            exit(1)
    else:
        print("No virtual environment to remove.")

def venv_python():
    return os.path.join(".venv", "Scripts", "python.exe") if os.name == "nt" else os.path.join(".venv", "bin", "python")

def run_build_in_venv():
    py = venv_python()
    subprocess.run([py, "-m", "pip", "install", "pyinstaller"], check=True)
    subprocess.run([py, "-c", "import make; make.build_executable()"], check=True)

if __name__ == "__main__":
    create_venv()
    print("im in venv now")
    py = venv_python()
    subprocess.run([py, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([py, "make.py"], check=True)
    exit(0)

os.run("/src/compile.py")
exit(0)