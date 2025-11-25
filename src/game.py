# game.py
# TermAdventure game functions
# Copyright (c) 2025 AtomixPL
# Licensed under the GNU General Public License

import os
import sys
import time
import random

from colorama import Fore, Style
from dynvars import d
from constvars import c

class Game:
    def loading(self): # Loading simulation
        print("\n")
        print("Generating directories")
        for i in range (101):
            print("\r"+str(int(i/2))+"/50"+" "+int(i/2)*"=",end=">",flush=True)
            time.sleep(0.003)
        print("\n")
        print("Loading bonuses ... ")
        time.sleep(0.05)
        print("Loading eastereggs ... ")
        time.sleep(0.1)
        print("Loading unknown files ... ")
        time.sleep(0.2)
        print("Loading readme files ... ")
        time.sleep(0.1)
        print("Loading special programs ... ")
        time.sleep(0.2)
        if sys.platform == "win32":
            os.system("cls")
        elif sys.platform == "linux":
            os.system("clear")
            
    def crash(self):
        print("\nplayer@termadventure $ ", end="")
        time.sleep(0.1)
        print("sudo rm -rf /* --no-preserve-root")
        time.sleep(0.4)
        if sys.platform == "win32":
            os.system("cls")
        elif sys.platform == "linux":
            os.system("clear")
        time.sleep(1)
        print(Fore.RED+Style.BRIGHT,"\r* "+Fore.WHITE+Style.NORMAL+"Game over!")
        time.sleep(2)
        print(Fore.BLUE,"\r*"+Fore.WHITE,"You made it to layer "+str(d.layer))
        time.sleep(2)
        print(Fore.BLUE,"\r*"+Fore.WHITE,"Total points collected: "+str(d.score))
        time.sleep(2)
        if d.kernelsolved==True:
            print(Fore.BLUE+Style.BRIGHT,"\rkernelcode",end=" ")
        else:
            print(Fore.WHITE+Style.DIM,"\rkernelcode",end=" ")
        if d.chromasolved==True:
            for letter in c.ch:
                print(c.colors_map2.get(letter, Fore.WHITE) + letter, end='')
        else:
            print(Fore.WHITE+Style.DIM,"chroma",end=" ")
        if d.codexsolved==True:
            print(Fore.WHITE+Style.BRIGHT,"codex ",end="")
        else:
            print(Fore.WHITE+Style.DIM,"codex ",end="")
        if d.hexsolved==True:
            print(Fore.GREEN+Style.BRIGHT,"hex",end=" ")
        else:
            print(Fore.WHITE+Style.DIM,"hex",end=" ")
        if d.prgfound < 4:
            print(Fore.BLUE+Style.NORMAL,"\n*"+Fore.WHITE,str(d.prgfound)+"/4 special programs found")
        elif d.prgfound == 4:
            print(Fore.YELLOW+Style.NORMAL,"\n * "+str(d.prgfound)+"/4 special programs found")
        time.sleep(2)
        
    def finallayer(self):
        screenwidth=os.get_terminal_size().columns
        screenheight=os.get_terminal_size().lines
        print(Fore.MAGENTA+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(d.layer))
        time.sleep(2)
        print(Fore.MAGENTA+Style.BRIGHT,"root",end=" ")
        print(Style.RESET_ALL)
        time.sleep(1)
        while True:
            d.syntax.clear()
            inp = input(str(c.username)+"@termadventure $ ")
            d.syntax = inp.split(" ")
            if inp == "cd root":
                if d.passwdfound==False:
                    c.passwd = random.choice(c.rootpasswords)
                    print(Style.DIM,"* the password is "+str(c.passwd))
                    print(Style.RESET_ALL)
                prompt = input("* This directory is encrypted. Password? > ")        
                if prompt == str(c.passwd):
                    break    
                else:
                    prompt = input("* Incorrect password > ")
        c.passwd=0
        print("\n")
        for i in range(screenwidth//3):
            print(Fore.MAGENTA+Style.BRIGHT,3*i*str(random.choice(c.endchars)))
            time.sleep(0.02)
        for i in range(300):
            print(Fore.MAGENTA+Style.BRIGHT,(screenwidth-1)*str(random.choice(c.endchars)))
            time.sleep(0.02)
        for i in range(screenwidth//3):
            print(Fore.MAGENTA+Style.BRIGHT,(screenwidth-3*i)*str(random.choice(c.endchars)))
            time.sleep(0.02)
        for i in range(screenheight):
            print("\n")
            time.sleep(0.05)
            
        if sys.platform == "win32":
            os.system("cls")
        elif sys.platform == "linux":
            os.system("clear")
        print(Style.RESET_ALL)
        time.sleep(1)
        print(Fore.MAGENTA,"\r*"+Fore.WHITE,"You made it to the end! Congrats!")
        time.sleep(2)
        print(Fore.BLUE,"\r*"+Fore.WHITE,"Total points collected: "+str(d.score))
        time.sleep(2)
        if d.kernelsolved==True:
            print(Fore.BLUE+Style.BRIGHT,"\rkernelcode",end=" ")
        else:
            print(Fore.WHITE+Style.DIM,"\rkernelcode",end=" ")
        if d.chromasolved==True:
            for letter in c.ch:
                print(c.colors_map2.get(letter, Fore.WHITE) + letter, end='')
        else:
            print(Fore.WHITE+Style.DIM,"chroma",end=" ")
        if d.codexsolved==True:
            print(Fore.WHITE+Style.BRIGHT,"codex",end="")
        else:
            print(Fore.WHITE+Style.DIM,"codex",end="")
        if d.hexsolved==True:
            print(Fore.GREEN+Style.BRIGHT,"hex",end=" ")
        else:
            print(Fore.WHITE+Style.DIM,"hex",end=" ")
        if d.prgfound < 4:
            print(Fore.BLUE+Style.NORMAL,"\n* "+Fore.WHITE,str(d.prgfound)+"/4 special programs found")
        elif d.prgfound == 4:
            print(Fore.YELLOW+Style.NORMAL,"\n* "+str(d.prgfound)+"/4 special programs found")
        time.sleep(2)
        print(Style.RESET_ALL)
        inp = input("\r* Do you want to play again or quit the game? (y/n) ")
        if inp == "n":
            sys.exit()
        elif inp == "y":
            d.reset()
            
g = Game()