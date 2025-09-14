import subprocess
import os
import sys
from pathlib import Path

current_dir = Path(__file__).parent.resolve()

def create_venv():
    if not os.path.exists(".venv"):
        print("Creating virtual environment...")
        # create venv using the same interpreter that runs this script
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True, cwd=str(current_dir))
        # install required packages into the venv without trying to "activate"
        py = venv_python()
        subprocess.run([py, "-m", "pip", "install", "--upgrade", "pip"], check=True, cwd=str(current_dir))
        subprocess.run([py, "-m", "pip", "install", "colorama", "pyinstaller"], check=True, cwd=str(current_dir))
    else:
        print("Virtual environment already exists.")

def remove_venv():
    if os.path.exists(".venv"):
        print("Removing virtual environment...")
        if os.name == 'nt':
            subprocess.run(['cmd.exe', '/c', 'rmdir /s /q .venv'], check=True, cwd=str(current_dir))
        elif os.name == 'posix':
            subprocess.run(['/bin/bash', '-c', 'rm -rf .venv'], check=True, cwd=str(current_dir))
        else:
            print("Unsupported OS for virtual environment removal.")
            exit(1)
    else:
        print("No virtual environment to remove.")

def venv_python():
    return os.path.join(".venv", "Scripts", "python.exe") if os.name == "nt" else os.path.join(".venv", "bin", "python")

def run_build_in_venv():
    py = venv_python()
    # ensure pyinstaller is present
    subprocess.run([py, "-m", "pip", "install", "pyinstaller"], check=True, cwd=str(current_dir))
    # import the module and call build_executable(); adjust module path if needed
    subprocess.run([py, "-c", "import src.compile as compile; compile.build_executable()"], check=True, cwd=str(current_dir))

if __name__ == "__main__":
    create_venv()
    print("in venv now")
    py = venv_python()
    # example: run a script inside the venv (script path relative to project root)
    # use 'src/compile.py' if that's the script file, or call run_build_in_venv() to call the function
    subprocess.run([py, "src/compile.py"], check=True, cwd=str(current_dir))
    # or to call the function directly:
    # run_build_in_venv()
    exit(0)

os.run("/src/compile.py")
exit(0)