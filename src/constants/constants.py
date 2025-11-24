# constants.py
# Constant variables, tables and dicts for TermAdventure
# Copyright (c) 2025 AtomixPL
# Licensed under the GNU General Public License

from colorama import Fore

class Constants:
        logo = r"""
  ______                    ___       __                 __                
 /_  __/__  _________ ___  /   | ____/ /   _____  ____  / /___  __________ 
  / / / _ \/ ___/ __ `__ \/ /| |/ __  / | / / _ \/ __ \/ __/ / / / ___/ _ \
 / / /  __/ /  / / / / / / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/
/_/  \___/_/  /_/ /_/ /_/_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/ 
"""
        info = """
Explore the seemingly infinite Linux kernel containing directories and files.
You may find a lot of interesting things, which can give you points.
But unknown files may delete your system (not literally), so be careful!
There are also readme files, which can contain codes for specific programs.
Reach layer 50 to get to the root directory. 
For the full guidebook, check out the README file in the repository."""
        codexgreeter = """
============
|| lorem! ||
============"""
        chromagreeter = """====================\n|---===chroma===---|\n===================="""
        chromagj = """===================================\n|------======GOOD JOB!======------|\n==================================="""
        endchars = ["/","@","#","$","%","&","*","!","?","^","~","`","-","_","=","+","|","{","}","[","]",":",";","<",">",",","."]
        help = """
ls - list directories
cd (dir) - change directory
cd .. - leave the directory
cat (text file) - read the content of the text file
(executable) - run the program or claim bonus"""
        latinnums={"unus": 1,
                "duo": 2,
                "tres": 3,
                "quattuor": 4,
                "quinque": 5,
                "sex": 6,
                "septem": 7,
                "octo": 8,
                "novem": 9}
        colors_map = {
            'r': Fore.RED,
            'g': Fore.GREEN,
            'y': Fore.YELLOW,
            'b': Fore.BLUE,
            'm': Fore.MAGENTA,
            'c': Fore.CYAN}
        colors_map2 = {
            'c': Fore.RED,
            'h': Fore.YELLOW,
            'r': Fore.GREEN,
            'o': Fore.CYAN,
            'm': Fore.BLUE,
            'a': Fore.MAGENTA}
        dirs=["bin","boot","dev","etc","lib","mnt","opt","proc","run","srv","sys","tmp","usr","var","dir","tux","linux","localhost","local","doc","share","tmpfs","home","udev","tty1","sbin","src",
            "lost+found","include","man","log","cache","lock","spool","sda1","sdb1","sdc1","hda1","hdb1","hdc1",
            "bin2","boot2","dev2","etc2","lib2","mnt2","opt2","proc","run2","srv2","sys2","tmp2","usr2","var2","dir2","tux2","linux2","localhost2","local2","doc2","share2","tmpfs2","home2","udev2",
            "tty2","sbin2","src2","lost+found2","include2","man2","log2","cache2","lock2","spool2","sda2","sdb2","sdc2","hda2","hdb2","hdc2",
            "bin3","boot3","dev3","etc3","lib3","mnt3","opt3","proc3","run3","srv3","sys3","tmp3","usr3","var3","dir3","tux3","linux3","localhost3","local3","doc3","share3","tmpfs3",
            "home3","udev3","tty3","sbin3","src3","lost+found3","include3","man3","log3","cache3","lock3","spool3","sda3","sdb3","sdc3","hda3","hdb3","hdc3",
            "bin4","boot4","dev4","etc4","lib4","mnt4","opt4","proc4","run4","srv4","sys4","tmp4","usr4","var4","dir4","tux4","linux4","localhost4","local4","doc4","share4",
            "tmpfs4","home4","udev4","tty4","sbin4","src4","lost+found4","include4","man4","log4","cache4","lock4","spool4","sda4","sdb4","sdc4"]   
        files=["bonus","easteregg","readme","readme2","readme3","unknown","codex","kernelcode","chroma","hex"]
        colors=["r","g","y","b","m","c"]
        ch=["c","h","r","o","m","a"]
        coloramas=[Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        specialreadmetexts=["Linux termadventure 6.15.5-zen1-1-zen x86_64 GNU/Linux",
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        ""","here are some points for you: ","your score is currently ","The password for the root directory is: "]
        readmetexts=["hello world","nothing to find here","thank you player, but the thing you're looking for is in another readme file!",
        "penguin is watching","nothing","if it works, don't touch it","it's free real estate","open source for the win","what's up","""
To do list:
- buy amd gpu
- get rid of windows
- install arch linux on first drive
- install gentoo on second drive
        ""","i am king terry the terrible",";-)","herzlich wilkommen","no looking back","keep it simple stupid"]
        rootpasswords=["********","123","root","admin","password","administrator","linuxthebest","excalibur","opensesame"]
        bonuses = [1000,2000,3000,4000,5000]
        username = 0
        passwd = 0
        
c = Constants()