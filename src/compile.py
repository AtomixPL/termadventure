import os
import subprocess

if os.name not in ['nt', 'posix']:
    print("Unsupported OS for this script.")
    exit(1)
else:
    print("Supported OS detected.")

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

def build_executable():
    from PyInstaller.__main__ import run
    args = ['--onefile', '--name', 'termadventure', 'src/termadventure.py']
    run(args)

def clean():
    if os.name == "posix":
        if os.path.exists("build"):
            os.system("rm -rf build")
        if os.path.exists("dist"):
            os.system("rm -rf dist")
        if os.path.exists("termadventure.spec"):
            os.remove("termadventure.spec")
    elif os.name == "nt":
        if os.path.exists("build"):
            os.system("rmdir /s /q build")
        if os.path.exists("dist"):
            os.system("rmdir /s /q dist")
        if os.path.exists("termadventure.spec"):
            os.remove("termadventure.spec")

def clean_except_executable():
    if os.path.exists("build"):
        os.system("rm -rf build")
    if os.path.exists("termadventure.spec"):
        os.remove("termadventure.spec")

def main():
    print("")
    print("")
    print("Welcome to the termadventure compiler")
    print("Please select an option:")
    print("1. Build Executable")
    print("2. Clean build files")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        build_executable()
        print("")
        print("Would you like to keep the build files? (y/N)")
        keep_files = input().lower()
        keep_files = (input().strip() or "n").lower()
        if keep_files == 'n':
            clean_except_executable()
            print("Build files cleaned, only executable kept.")
            print("")
            main()
        else:
            main()
    elif choice == "2":
        clean()
        print("")
        print("Build files cleaned.")
        print("")
        main()
    elif choice == "3":
        print("")
        print("Exiting.")
        print("")
        remove_venv()
        exit(0)
        
    else:
        print("")
        print("Invalid choice. Please try again.")
        print("")
        main()

if __name__ == "__main__":
    main()



