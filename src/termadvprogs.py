# termadvprogs.py
# TermAdventure in-game programs functions
# Copyright (c) 2025 Atomix
# Licensed under the GNU General Public License

import time
import random

from colorama import Fore, Style
from dynvars import d
from constvars import c

class Programs:
    def genspecprogs(self): # If readme of program found then generate the program 
            if d.codexread==True and d.codexsolved==False:
                d.codexprg_chance = random.randint(1,20)
            if d.kernelread==True and d.kernelsolved==False:
                d.kernelcodeprg_chance = random.randint(1,20)
            if d.chromaread==True and d.chromasolved==False:
                d.chromaprg_chance = random.randint(1,20)
            if d.codexsolved==True and d.hexsolved==False:
                d.hexprg_chance = random.randint(1,20)
                
    def readlorem(self):
            print(c.codexgreeter)
            time.sleep(0.5)
            print(Style.RESET_ALL)
            print("typus in codice ",end="")
            while True:
                inp = input("-> ")
                if inp == str(d.codexnum[0])+str(d.codexnum[1])+str(d.codexnum[2]):
                    break
                else:
                    print("codicem invalidum ",end="")
            print("""               _
gratulationes! L punctorum""")
            print("codex: +500 000 pts")
            d.score+=500000
            d.codexsolved=True
            d.codexread=True
            d.codexprg_chance = 0
            d.file.remove("codex")
            d.prgfound+=1

    def readkernel(self):
        print("-= KERNEL CODE CHECK =-")
        while True:
            inp = input("Enter code here: ")
            if inp == str(d.kernelcode):
                break
            else:
                print(Fore.RED,"Incorrect code ",end="")
        print("kernelcode: +100 000 pts")
        d.score+=100000
        d.kernelsolved=True
        d.kernelread=True
        d.kernelcodeprg_chance = 0
        d.file.remove("kernelcode")
        d.prgfound+=1

    def readchroma(self):
        for color in c.coloramas:
            print(color + c.chromagreeter, end='\x1b[2A'+'\r')
            time.sleep(0.1)
        print("\n\n")
        while True:
            inp = input("\rPlease enter color code: ")
            if inp == str(d.chromacode):
                break
            else:
                print(Fore.WHITE,"\rIncorrect code ",end="")
        for i in range(3):
            for color in c.coloramas:
                print(color + c.chromagj, end='\x1b[2A'+'\r')
                time.sleep(0.03)
        print("\n\n")
        print(Fore.WHITE+"chroma: +200 000 pts")
        d.score+=200000
        d.chromasolved=True
        d.chromaread=True
        d.chromaprg_chance = 0
        d.file.remove("chroma")
        d.chromacode=0
        d.prgfound+=1
        
    def readhex(self):
        hexes = []
        for i in range(6):
            hexes.insert(i,[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])])
            
        r = str(hex(random.randint(16,255))[2:])
        for i in range(5): #five reiterations
            row = random.randint(0, len(hexes) - 1)
            col = random.randint(0, len(hexes[row]) - 1)
            hexes[row][col] = r
            
        print(Fore.GREEN,"\n-= HEX VIEWER =-")
        for i in range(6):
            print(Fore.WHITE,*hexes[i])

        print(Fore.GREEN,"\n*"+Fore.WHITE,"Find five reiterations")
        print(Fore.GREEN,"\r*"+Fore.WHITE,"Enter here ",end="")
        while True:
            inp = input("> ")
            if inp == r:
                break
            elif inp != r:
                print(Fore.RED,"\r*"+Fore.WHITE,"Wrong number ",end="")
            
        print(Fore.YELLOW,"\n* Correct!")
        time.sleep(0.5)
        hexes.clear()
        print("\n")
        print(Fore.GREEN,"-= HEX VIEWER =-")
        for i in range(8):
            hexes.insert(i,[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])])
            
        r = str(hex(random.randint(16,255))[2:])
        for i in range(5): #five reiterations
            row = random.randint(0, len(hexes) - 1)
            col = random.randint(0, len(hexes[row]) - 1)
            hexes[row][col] = r
        
        for i in range(8):
            print(Fore.WHITE,*hexes[i])
                
        print("\n")
        print(Fore.GREEN,"\r*"+Fore.WHITE,"Enter here ",end="")
        while True:
            inp = input("> ")
            if inp == r:
                break
            elif inp != r:
                print(Fore.RED,"\r*"+Fore.WHITE,"Wrong number ",end="")
                
        print(Fore.YELLOW,"\n* Correct!")
        time.sleep(0.5)
        hexes.clear()
        print("\n")
        print(Fore.GREEN,"-= HEX VIEWER =-")
        for i in range(10):
            hexes.insert(i,[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])]
                        +[str(hex(random.randint(16,255))[2:])]+[str(hex(random.randint(16,255))[2:])])
            
        r = str(hex(random.randint(16,255))[2:])
        for i in range(5): #five reiterations
            row = random.randint(0, len(hexes) - 1)
            col = random.randint(0, len(hexes[row]) - 1)
            hexes[row][col] = r
        
        for i in range(10):
            print(Fore.WHITE,*hexes[i])  
        
        print("\n")
        print(Fore.GREEN,"\r*"+Fore.WHITE,"Enter here ",end="")
        while True:
            inp = input("> ")
            if inp == r:
                break
            elif inp != r:
                print(Fore.RED,"\r*"+Fore.WHITE,"Wrong number ",end="")
        
        print(Fore.YELLOW,"\n* Correct!")
        time.sleep(0.5)
        print(Fore.WHITE,"hex: 1 000 000 pts")
        d.score+=1000000
        d.hexsolved=True
        d.solvedall=True
        d.prgfound+=1
        print(Fore.YELLOW+Style.BRIGHT,"\r* All special programs found! +500 000 pts")
        d.score+=500000
        d.file.remove("hex")

p = Programs()
