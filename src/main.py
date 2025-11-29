# main.py
# Copyright (c) 2025 Atomix
# Licensed under the GNU General Public License

import time
import random
import sys
    
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    if sys.platform=="win32":
        print(r"""Please launch the game using Python from \venv\Scripts directory.""")
    elif sys.platform=="linux":
        print("Please launch the game using Python from /venv/bin directory.")
    sys.exit()
    
from constvars import c
from dynvars import d
from game import g
from termadvfiles import f
from termadvprogs import p


print(Fore.BLUE+Style.BRIGHT+c.logo, end="") # Print menu
print(Fore.WHITE,"Copyright (c) 2025 Atomix"+Style.NORMAL,"                                         v1.1.0")
print(Style.RESET_ALL)
print(Fore.BLUE,"* "+Fore.WHITE+Style.BRIGHT+"play"+Style.NORMAL,"(p) - start the adventure")
print(Fore.BLUE,"* "+Fore.WHITE+Style.BRIGHT+"info"+Style.NORMAL,"(i) - about the game")
print(Fore.BLUE,"* "+Fore.WHITE+Style.BRIGHT+"quit"+Style.NORMAL,"(q) - exit the program")

while True:
    inp = input(Style.RESET_ALL+"\nplayer@termadventure $ ")

    if inp == "info" or inp == "i":
        print(c.info)
    if inp == "quit" or inp == "q":
        sys.exit()
    if inp == "play" or inp == "p":
        break

while True:
    inp = input("\n* Type in your username (must be lowercase and cannot contain spaces): ")
    if " " in str(inp) or str(inp) == "":
        print("Try again")
    else:
        c.username = inp.lower()
        break
            
while True:
    
    g.loading()
    print("\n"+Fore.BLUE+Style.NORMAL,"*"+Fore.WHITE,"Let's go!")
    time.sleep(2)
    print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(d.layer))
    
    print(Fore.BLUE+Style.BRIGHT,"home",end=" ")
    while True:
        print(Style.RESET_ALL)
        inp = input(str(c.username)+"@termadventure $ ")
        if inp == "cd home":
            break
        
        elif inp == "quit" or inp == "q":
            sys.exit()
            
        elif inp == "help":
            print(c.help)
        
    d.layer+=1
    d.score+=100
    print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(d.layer),end="  ")
    print(Fore.GREEN,"+100 pts")
    for i in range(random.randint(4,7)):
        d.names.append(str(random.choice(c.dirs)))
        print(Fore.BLUE+Style.BRIGHT,d.names[i],end=" ")
        
    for i in d.names:
        for i in range(random.randint(4,7)):
            d.gendir.append(str(random.choice(c.dirs)))
        d.dir.append(list(d.gendir))
        d.gendir.clear()
               
    while d.layer < 50:
        
        if inp == "cd .." and d.inemptydir == False and d.wentbackempty == False:
            print(Fore.YELLOW,"*"+Fore.WHITE,"Sorry, you can't go back",end=" ")
            
        if inp == "quit" or inp == "q":
            sys.exit()
            
        if inp == "help":
            print(c.help)
            
        if inp == "ls":
            if d.inemptydir==False:
                f.listfiles()
            elif d.inemptydir==True:
                print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end=" ")

        if d.inemptydir == True:
            print(Style.RESET_ALL)
            inp = input(str(c.username)+"@termadventure $ ")
            d.syntax = inp.split(" ")
            d.syntax+=[".."]
            
        if inp == "cd .." and d.inemptydir == True and d.wentbackempty == False: #cd .. when entered empty
            d.layer-=1
            print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(d.layer))
            f.listfiles()
            d.wentbackempty=True
            d.inemptydir=False

        if d.wentbackempty == False and d.inemptydir == False:
            print(Style.RESET_ALL)
            inp = input(str(c.username)+"@termadventure $ ")
            d.syntax = inp.split(" ")
            d.syntax+=[".."]
            
            if inp == str(d.syntax[0])+" "+str(d.syntax[1]):
                if d.syntax[1] in d.names: #cd dest
                    d.layer+=1
                    if d.layer == 50:
                        break
                    empty_chance = random.randint(1,10)
                    print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(d.layer),end="  ")
                    
                    if empty_chance < 9:
                        
                        print(Fore.GREEN,"+100 pts")
                        d.score+=100
                        d.memory.clear()
                        d.memory+=d.dir
                        d.names_memory.clear()
                        d.names_memory+=d.names
                        d.names.clear()
                        d.dir.clear()
                        d.file_memory.clear()
                        d.file_memory+=d.file
                        d.file.clear()
                        d.readme.clear()
                        d.readme2.clear()
                        d.readme3.clear()
                        d.bonus_chance = random.randint(1,15)
                        d.easter_chance = random.randint(1,15)
                        d.readme_chance = random.randint(1,15)
                        d.amethyst_chance = random.randint(1,50)
                        d.diamond_chance = random.randint(1,60)
                        d.ruby_chance = random.randint(1,70)
                        p.genspecprogs()
                        
                        for i in range(len(d.names_memory)):
                            if d.syntax[1] == d.names_memory[i]:
                                f.gendirs(i)
                                break
                        f.genfiles()
                        
                    elif empty_chance >= 9:
                        f.mkempty() 
                        d.inemptydir=True
                        print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end=" ")
                    
            if inp == c.files[0]:
                if inp == "bonus" and d.syntax[0] in d.file: #bonus
                    bonusscore = random.choice(c.bonuses)
                    print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                    d.score+=bonusscore
                    d.file.remove("bonus")
                        
            if inp == c.files[1]:
                if inp == "easteregg" and d.syntax[0] in d.file: #easteregg
                    print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10 000 pts",end=" ")
                    d.score+=10000
                    d.file.remove("easteregg")
                    
            if inp == "cat "+str(c.files[2]):
                if c.files[2] in d.file:  #readme files
                    f.readfile1()
                        
            if inp == "cat "+str(c.files[3]):
                if c.files[3] in d.file:
                    f.readfile2()
                        
            if inp == "cat "+str(c.files[4]):
                if c.files[4] in d.file:
                    f.readfile3()

            if inp == c.files[5]:
                if inp == "ruby" and d.syntax[0] in d.file:
                    print(Fore.RED+Style.BRIGHT,"* Shiny! +500 000 pts",end=" ")
                    d.score+=500000
                    d.file.remove("ruby")
                    
                        
            if inp == c.files[6]:
                if c.files[6] in d.file:
                    p.readlorem()
            if inp == c.files[7]:
                if c.files[7] in d.file:
                    p.readkernel()
            if inp == c.files[8]:
                if c.files[8] in d.file:
                    p.readchroma()
            if inp == c.files[9]:
                if c.files[9] in d.file:
                    p.readhex()
            
            if inp == c.files[10]:
                if inp == "amethyst" and d.syntax[0] in d.file: #amesthyst
                    print(Fore.MAGENTA+Style.BRIGHT,"* Amethyst found! +50 000 pts",end=" ")
                    d.score+=50000
                    d.file.remove("amethyst")
            
            if inp == c.files[11]:
                if inp == "diamond" and d.syntax[0] in d.file: #diamond
                    print(Fore.CYAN+Style.BRIGHT,"* Diamond found! +100 000 pts",end=" ")
                    d.score+=100000
                    d.file.remove("diamond")
            
        if d.wentbackempty == True and d.inemptydir == False:
            print(Style.RESET_ALL)
            inp = input(str(c.username)+"@termadventure $ ")
            d.syntax = inp.split(" ")
            d.syntax+=[".."]
            
            if inp == str(d.syntax[0])+" "+str(d.syntax[1]):  
                if d.syntax[0] == "cd" and d.syntax[1] in d.names: #cd (newdest)
                    
                    if d.syntax[1] in d.names: #cd dest
                        d.layer+=1
                        empty_chance = random.randint(1,10)
                        d.bonus_chance = random.randint(1,15)
                        d.easter_chance = random.randint(1,15)
                        d.readme_chance = random.randint(1,15)
                        d.amethyst_chance = random.randint(1,50)
                        d.diamond_chance = random.randint(1,60)
                        d.ruby_chance = random.randint(1,70)
                        p.genspecprogs()
                            
                        print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(d.layer),end="  ")
                        if empty_chance < 9:
                            for i in range(len(d.names)):
                                if d.syntax[1] == d.names[i]:
                                    f.gendirsback(i)
                                    break
                            if d.inemptydir == False:
                                f.genfiles()
                        
                        elif empty_chance >= 9:
                            f.mkempty()
                            d.inemptydir=True
                            print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end=" ")
                        d.wentbackempty=False
                        
                if inp == "cd .." and d.wentbackempty == True:
                    print(Fore.YELLOW,"*"+Fore.WHITE,"You can't go back now!",end=" ")
                    
            if inp == "cat "+str(c.files[2]):
                if c.files[2] in d.file:  #readme files
                    f.readfile1()
            if inp == "cat "+str(c.files[3]):
                if c.files[3] in d.file:
                    f.readfile2()
            if inp == "cat "+str(c.files[4]):
                if c.files[4] in d.file:
                    f.readfile3()
                    
            if inp == c.files[5]:
                if inp == "ruby" and d.syntax[0] in d.file:
                    print(Fore.RED+Style.BRIGHT,"* Shiny! +500 000 pts",end=" ")
                    d.score+=500000
                    d.file.remove("ruby")
                            
            if inp == c.files[6]:           
                if c.files[6] in d.file:
                    p.readlorem()
            if inp == c.files[7]:
                if c.files[7] in d.file:
                    p.readkernel()
            if inp == c.files[8]:
                if c.files[8] in d.file:
                    p.readchroma()
            if inp == c.files[9]:
                if c.files[9] in d.file:
                    p.readhex()
            
            if inp == c.files[10]:
                if inp == "amethyst" and d.syntax[0] in d.file: #amesthyst
                    print(Fore.MAGENTA+Style.BRIGHT,"* Amethyst found! +50 000 pts",end=" ")
                    d.score+=50000
                    d.file.remove("amethyst")
            
            if inp == c.files[11]:
                if inp == "diamond" and d.syntax[0] in d.file: #diamond
                    print(Fore.CYAN+Style.BRIGHT,"* Diamond found! +100 000 pts",end=" ")
                    d.score+=100000
                    d.file.remove("diamond")
                    
            if inp == "bonus" and d.syntax[0] in d.file: #bonus
                    bonusscore = random.choice(c.bonuses)
                    print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                    d.score+=bonusscore
                    d.file.remove("bonus")
                        
            if d.syntax[0] == "easteregg" and d.syntax[0] in d.file: #easteregg
                print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10 000 pts",end=" ")
                d.score+=10000
                d.file.remove("easteregg")

    if d.layer == 50:
        g.finallayer()