# TermAdventure
# Copyright (c) 2025 AtomixPL
# Licensed under the MIT License

# dir mechanics 
# print("dir "+str(dir))
# print("memory "+str(memory))
# print("names "+str(names))
# print("names_memory "+str(names_memory))         

import time
import random
import os
import sys
    
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    if sys.platform=="win32":
        print(r"""Please launch the game using Python from \venv\Scripts directory.""")
    elif sys.platform=="linux":
        print("Please launch the game using Python from /venv/bin directory.")
    sys.exit()
    
score = 0
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
scorelist = {
    'date': 0,
    'time': 0,
    'score': 0,
    'layer': 0,
    'specprogs': 0}
dirs=["bin","boot","dev","etc","lib","mnt","opt","proc","run","srv","sys","tmp","usr","var","dir","tux","linux","localhost","local","doc","share","tmpfs","home","udev","tty1","sbin","src",
      "lost+found","include","man","log","cache","lock","spool","sda1","sdb1","sdc1",
      "bin2","boot2","dev2","etc2","lib2","mnt2","opt2","proc","run2","srv2","sys2","tmp2","usr2","var2","dir2","tux2","linux2","localhost2","local2","doc2","share2","tmpfs2","home2","udev2",
      "tty2","sbin2","src2","lost+found2","include2","man2","log2","cache2","lock2","spool2","sda2","sdb2","sdc2",
      "bin3","boot3","dev3","etc3","lib3","mnt3","opt3","proc3","run3","srv3","sys3","tmp3","usr3","var3","dir3","tux3","linux3","localhost3","local3","doc3","share3","tmpfs3",
      "home3","udev3","tty3","sbin3","src3","lost+found3","include3","man3","log3","cache3","lock3","spool3","sda3","sdb3","sdc3",
      "bin4","boot4","dev4","etc4","lib4","mnt4","opt4","proc4","run4","srv4","sys4","tmp4","usr4","var4","dir4","tux4","linux4","localhost4","local4","doc4","share4",
      "tmpfs4","home4","udev4","tty4","sbin4","src4","lost+found4","include4","man4","log4","cache4","lock4","spool4","sda4","sdb4","sdc4"]   
files=["bonus","easteregg","readme","readme2","readme3","unknown","codex","kernelcode","chroma","hex"]
colors=["r","g","y","b","m","c"]
ch=["c","h","r","o","m","a"]
rainbow = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
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
print(Fore.BLUE+Style.BRIGHT,r"""
  ______                    ___       __                 __                
 /_  __/__  _________ ___  /   | ____/ /   _____  ____  / /___  __________ 
  / / / _ \/ ___/ __ `__ \/ /| |/ __  / | / / _ \/ __ \/ __/ / / / ___/ _ \
 / / /  __/ /  / / / / / / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/
/_/  \___/_/  /_/ /_/ /_/_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/ 
""", end="")
print(Fore.WHITE,"Copyright (c) 2025 AtomixPL"+Style.NORMAL,"                                      v1.0.0")
print(Style.RESET_ALL)
print(Fore.BLUE,"* "+Fore.WHITE+Style.BRIGHT+"play"+Style.NORMAL,"(p) - start the adventure")
print(Fore.BLUE,"* "+Fore.WHITE+Style.BRIGHT+"info"+Style.NORMAL,"(i) - about the game")
print(Fore.BLUE,"* "+Fore.WHITE+Style.BRIGHT+"quit"+Style.NORMAL,"(q) - exit the program")

while True:
    inp = input(Style.RESET_ALL+"\nplayer@termadventure $ ")

    if inp == "info" or inp == "i":
        print("""           
Explore the seemingly infinite Linux kernel containing directories and files.
You may find a lot of interesting things, which can give you points.
But unknown files may delete your system (not literally), so be careful!
There are also readme files, which can contain codes for specific programs.
Reach layer 50 to get to the root directory. 
For the full guidebook, check out the README file in the repository.""")
        
    if inp == "quit" or inp == "q":
        sys.exit()
    if inp == "play" or inp == "p":
        break

while True:
    inp = input("\n* Type in your username (must be lowercase and cannot contain spaces): ")
    if " " in str(inp):
        print("Try again")
    else:
        username = inp.lower()
        break

def loading():
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
        
def listfiles():
    global names,files,file
    for i in range(len(names)):
        print(Fore.BLUE+Style.BRIGHT,names[i],end=" ")
    if "bonus" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end=" ")
    if "codex" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[6],end=" ")
    if "kernelcode" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[7],end=" ")
    if "chroma" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[8],end=" ")
    if "hex" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[9],end=" ")
    if "easteregg" in file:
        print(Fore.YELLOW+Style.BRIGHT,files[1],end=" ")
    if "unknown" in file:
        print(Fore.RED+Style.BRIGHT,files[5],end=" ")
    if "readme" in file:
        print(Fore.WHITE+Style.NORMAL,files[2],end=" ")
    if "readme2" in file:
        print(Fore.WHITE+Style.NORMAL,files[3],end=" ")
    if "readme3" in file:
        print(Fore.WHITE+Style.NORMAL,files[4],end=" ")
    
def genspecprogs():
    global codexprg_chance,kernelcodeprg_chance,chromaprg_chance,codexsolved,hexprg_chance
    if codexread==True and codexsolved==False:
        codexprg_chance = random.randint(1,20)
    if kernelread==True and kernelsolved==False:
        kernelcodeprg_chance = random.randint(1,20)
    if chromaread==True and chromasolved==False:
        chromaprg_chance = random.randint(1,20)
    if codexsolved==True and hexsolved==False:
        hexprg_chance = random.randint(1,20)
    
def gendirs(x):
    global memory,names,gendir,dir,dirs
    for i in range(len(memory[x])):
        print(Fore.BLUE+Style.BRIGHT,memory[x][i],end=" ")
        names.append(memory[x][i])
    for i in memory[x]:
        for i in range(random.randint(4,7)):
            gendir.append(str(random.choice(dirs)))
        dir.append(list(gendir))
        gendir.clear()

def genfiles():
    if bonus_chance > 8:
        file.append(str(files[0]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end=" ")
    if codexprg_chance >= 16:
        file.append(str(files[6]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[6],end=" ")
    if kernelcodeprg_chance >= 16:
        file.append(str(files[7]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[7],end=" ")
    if chromaprg_chance >= 16:
        file.append(str(files[8]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[8],end=" ")
    if hexprg_chance >= 18:
        file.append(str(files[9]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[9],end=" ")
    if easter_chance > 14:
        file.append(str(files[1]))
        print(Fore.YELLOW+Style.BRIGHT,files[1],end=" ")                      
    if unknown_chance > 10:
        file.append(str(files[5]))
        print(Fore.RED+Style.BRIGHT,files[5],end=" ")
    if readme_chance > 7:
        readmenum = random.randint(1,3)
        if readmenum == 1:
            file.append(str(files[2]))
            print(Fore.WHITE+Style.NORMAL,files[2],end=" ")   
        elif readmenum == 2:
            file.append(str(files[2]))
            file.append(str(files[3]))
            print(Fore.WHITE+Style.NORMAL,files[2],end=" ")
            print(Fore.WHITE+Style.NORMAL,files[3],end=" ")
        elif readmenum == 3:
            file.append(str(files[2]))
            file.append(str(files[3]))
            file.append(str(files[4]))
            print(Fore.WHITE+Style.NORMAL,files[2],end=" ")
            print(Fore.WHITE+Style.NORMAL,files[3],end=" ")
            print(Fore.WHITE+Style.NORMAL,files[4],end=" ")     

def mkempty():
    global syntax,names,dir
    if syntax[1] == names[0]:
        dir[0].append("empty")
    elif syntax[1] == names[1]:
        dir[1].append("empty")
    elif syntax[1] == names[2]:
        dir[2].append("empty")
    elif syntax[1] == names[3]:
        dir[3].append("empty")
    elif syntax[1] == names[4]:
        dir[4].append("empty")
    elif syntax[1] == names[5]:
        dir[5].append("empty")
    elif syntax[1] == names[6]:
        dir[6].append("empty")
        
def readfile1():
    global kernelread,codexread,chromaread,score,kernelcode_chance,codex_chance,chroma_chance,passwd_chance,kernelcode,codexnum,chromacode,passwd,passwdfound
    if not readme:
        kernelcode_chance = 0
        codex_chance = 0
        chroma_chance = 0
        bonus_chance = random.randint(1,20)
        readmescore = random.randint(1,20)
        if kernelread==False:
            kernelcode_chance = random.randint(1,40)
        if codexread==False:
            codex_chance = random.randint(1,40) 
        if chromaread==False:
            chroma_chance = random.randint(1,40)
        bonus_chance = random.randint(1,20)
        readmescore = random.randint(1,20)
        passwd_chance = random.randint(1,40)
        
        if kernelcode_chance >= 33 and kernelsolved==False and kernelread==False:
            if kernelread == False:
                print(specialreadmetexts[0],end=" ")
                kernelcode=random.randint(111,999)
                print(kernelcode,end="")
                readme.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                kernelread=True
                kernelcode_chance = 0
                
        elif codex_chance >= 33 and codexsolved==False and codexread==False and kernelsolved==True and chromasolved==True:
            if codexread == False:
                codex = dict(random.sample(list(latinnums.items()), 3))
                print(specialreadmetexts[1])
                print(*codex.keys(), end="")
                readme.append(str(specialreadmetexts[1]))
                readme.append("".join(codex.keys()))
                codexnum = list(codex.values())
                codexread=True
                codex_chance = 0
                
        elif chroma_chance >= 33 and chromasolved==False and chromaread==False and kernelsolved==True:
            if chromaread == False:
                chroma = random.sample(colors,len(colors))
                for i in range(len(chroma)):
                    color = colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
                readme.append(''.join(chroma))
                chromacode = ''.join(chroma)
                chromaread=True
                chroma_chance = 0
                
        elif passwd_chance >= 37 and passwdfound == False:
            passwd = random.choice(rootpasswords)
            readme.append(specialreadmetexts[4]+str(passwd))
            print(*readme,end="")
            passwdfound=True
                        
        elif bonus_chance == 20:
            bonusscore = random.choice(bonuses)
            print(specialreadmetexts[2],end="")
            print(bonusscore)
            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
            score+=bonusscore
            readme.append(str(specialreadmetexts[2]+str(bonusscore)))
            
        elif readmescore == 20:
            readme.append(specialreadmetexts[3]+str(score))
            print(*readme,end="")
            
        elif kernelcode_chance  < 33 or codex_chance < 33 or chroma_chance < 33 or passwd_chance < 37 or bonus_chance != 20 or readmescore != 20 or kernelsolved == True or codexsolved == True:
            readme.append(str(random.choice(readmetexts)))
            print(*readme,end="\r")
    else:
        if chromacode != 0:
            for i in range(len(chroma)):
                    color = colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
        else: 
            print(*readme,end="\r")
            
def readfile2():
    global kernelread,codexread,chromaread,score,kernelcode_chance,codex_chance,chroma_chance,passwd_chance,kernelcode,codexnum,chromacode,passwd,passwdfound
    if not readme2:
        if kernelread==False:
            kernelcode_chance = random.randint(1,20)
        if codexread==False:
            codex_chance = random.randint(1,30) 
        if chromaread==False:
            chroma_chance = random.randint(1,40)
        bonus_chance = random.randint(1,20)
        readmescore = random.randint(1,20)
        passwd_chance = random.randint(1,40)
        
        if kernelcode_chance >= 33 and kernelsolved==False and kernelread==False:
            if kernelread == False:
                print(specialreadmetexts[0],end=" ")
                kernelcode=random.randint(111,999)
                print(kernelcode,end="")
                readme2.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                kernelread=True
                kernelcode_chance = 0
                
        elif codex_chance >= 33 and codexsolved==False and codexread==False and kernelsolved==True and chromasolved==True:
            if codexread == False:
                codex = dict(random.sample(list(latinnums.items()), 3))
                print(specialreadmetexts[1])
                print(*codex.keys(), end="")
                readme2.append(str(specialreadmetexts[1]))
                readme2.append("".join(codex.keys()))
                codexnum = list(codex.values())
                codexread=True
                codex_chance = 0
        
        elif chroma_chance >= 33 and chromasolved==False and chromaread==False and kernelsolved==True:
            if chromaread == False:
                chroma = random.sample(colors,len(colors))
                for i in range(len(chroma)):
                    color = colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
                print(Style.RESET_ALL)
                readme2.append(''.join(chroma))
                chromacode = ''.join(chroma)
                chromaread=True
                chroma_chance = 0
                
        elif passwd_chance >= 37 and passwdfound == False:
            passwd = random.choice(rootpasswords)
            readme2.append(specialreadmetexts[4]+str(passwd))
            print(*readme2,end="")
            passwdfound=True
        
        elif bonus_chance == 20:
            bonusscore = random.choice(bonuses)
            print(specialreadmetexts[2],end="")
            print(bonusscore)
            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
            score+=bonusscore
            readme2.append(str(specialreadmetexts[2]+str(bonusscore)))
        
        elif readmescore == 20:
            readme2.append(specialreadmetexts[3]+str(score))
            print(*readme2,end="")
        
        elif kernelcode_chance  < 33 or codex_chance < 33 or chroma_chance < 33 or passwd_chance < 37 or bonus_chance != 20 or readmescore != 20 or kernelsolved == True or codexsolved == True:
            readme2.append(str(random.choice(readmetexts)))
            print(*readme2,end="\r")
    else:
        if chromacode != 0:
            for i in range(len(chroma)):
                    color = colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
        else: 
            print(*readme2,end="\r")
            
def readfile3():
    global kernelread,codexread,chromaread,score,kernelcode_chance,codex_chance,chroma_chance,passwd_chance,kernelcode,codexnum,chromacode,passwd,passwdfound
    if not readme3:
        if kernelread==False:
            kernelcode_chance = random.randint(1,20)
        if codexread==False:
            codex_chance = random.randint(1,30) 
        if chromaread==False:
            chroma_chance = random.randint(1,40)
        bonus_chance = random.randint(1,20)
        readmescore = random.randint(1,20)
        passwd_chance = random.randint(1,40)
        
        if kernelcode_chance >= 33 and kernelsolved==False and kernelread==False:
            if kernelread == False:
                print(specialreadmetexts[0],end=" ")
                kernelcode=random.randint(111,999)
                print(kernelcode,end="")
                readme3.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                kernelread=True
                kernelcode_chance = 0
                
        elif codex_chance >= 33 and codexsolved==False and codexread==False and kernelsolved==True and chromasolved==True:
            if codexread == False:
                codex = dict(random.sample(list(latinnums.items()), 3))
                print(specialreadmetexts[1])
                print(*codex.keys(), end="")
                readme3.append(str(specialreadmetexts[1]))
                readme3.append("".join(codex.keys()))
                codexnum = list(codex.values())
                codexread=True
                codex_chance = 0
            
        elif chroma_chance >= 33 and chromasolved==False and chromaread==False and kernelsolved==True:
            if chromaread == False:
                chroma = random.sample(colors,len(colors))
                for i in range(len(chroma)):
                    color = colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
                print(Style.RESET_ALL)
                readme3.append(''.join(chroma))
                chromacode = ''.join(chroma)
                chromaread=True
                chroma_chance = 0
                
        elif passwd_chance >= 37 and passwdfound == False:
            passwd = random.choice(rootpasswords)
            readme3.append(specialreadmetexts[4]+str(passwd))
            print(*readme3,end="")
            passwdfound=True
        
        elif bonus_chance == 20:
            bonusscore = random.choice(bonuses)
            print(specialreadmetexts[2],end="")
            print(bonusscore)
            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
            score+=bonusscore
            readme3.append(str(specialreadmetexts[2]+str(bonusscore)))
        
        elif readmescore == 20:
            readme3.append(specialreadmetexts[3]+str(score))
            print(*readme3,end="")
            
        elif kernelcode_chance  < 33 or codex_chance < 33 or chroma_chance < 33 or passwd_chance < 37 or bonus_chance != 20 or readmescore != 20 or kernelsolved == True or codexsolved == True:
            readme3.append(str(random.choice(readmetexts)))
            print(*readme3,end="\r")
    else:
        if chromacode != 0:
            for i in range(len(chroma)):
                    color = colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
        else: 
            print(*readme3,end="\r")
         
def crash():
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
    print(Fore.BLUE,"\r*"+Fore.WHITE,"You made it to layer "+str(layer))
    time.sleep(2)
    print(Fore.BLUE,"\r*"+Fore.WHITE,"Total points collected: "+str(score))
    time.sleep(2)
    if kernelsolved==True:
        print(Fore.BLUE+Style.BRIGHT,"\rkernelcode",end=" ")
    else:
        print(Fore.WHITE+Style.DIM,"\rkernelcode",end=" ")
    if chromasolved==True:
        for letter in ch:
            print(colors_map2.get(letter, Fore.WHITE) + letter, end='')
    else:
        print(Fore.WHITE+Style.DIM,"chroma",end=" ")
    if codexsolved==True:
        print(Fore.WHITE+Style.BRIGHT,"codex ",end="")
    else:
        print(Fore.WHITE+Style.DIM,"codex ",end="")
    if hexsolved==True:
        print(Fore.GREEN+Style.BRIGHT,"hex",end=" ")
    else:
        print(Fore.WHITE+Style.DIM,"hex",end=" ")
    if prgfound < 4:
        print(Fore.BLUE+Style.NORMAL,"\n*"+Fore.WHITE,str(prgfound)+"/4 special programs found")
    elif prgfound == 4:
        print(Fore.YELLOW+Style.NORMAL,"\n * "+str(prgfound)+"/4 special programs found")
    time.sleep(2)
    
def readlorem():
    global codexnum,codexsolved,codexread,codexprg_chance,score,prgfound
    print("""
============
|| lorem! ||
============""")
    time.sleep(0.5)
    print(Style.RESET_ALL)
    print("typus in codice ",end="")
    while True:
        inp = input("-> ")
        if inp == str(codexnum[0])+str(codexnum[1])+str(codexnum[2]):
            break
        else:
            print("codicem invalidum ",end="")
    print("""               _
gratulationes! L punctorum""")
    print("codex: +50 000 pts")
    score+=30000
    codexsolved=True
    codexread=True
    codexprg_chance = 0
    file.remove("codex")
    prgfound+=1

def readkernel():
    global kernelcode,kernelsolved,kernelread,kernelcodeprg_chance,score,prgfound
    print(Fore.WHITE,"-= Kernel code check ",end="")
    while True:
        inp = input("> ")
        if inp == str(kernelcode):
            break
        else:
            print(Fore.WHITE,"-= Incorrect code ",end="")
    print("kernelcode: +20 000 pts")
    score+=20000
    kernelsolved=True
    kernelread=True
    kernelcodeprg_chance = 0
    file.remove("kernelcode")
    prgfound+=1

def readchroma():
    global chromacode,chromasolved,chromaread,chromaprg_chance,score,prgfound
    greeter=("""====================\n|---===chroma===---|\n====================""")
    for color in coloramas:
        print(color + greeter, end='\x1b[2A'+'\r')
        time.sleep(0.1)
    print("\n\n")
    print(Fore.WHITE,"\rEnter code: ",end="")
    while True:
        inp = input("=> ")
        if inp == str(chromacode):
            break
        else:
            print(Fore.WHITE,"\rIncorrect code ",end="")
    goodjob=("""===================================\n|------======GOOD JOB!======------|\n===================================""")
    for i in range(3):
        for color in coloramas:
            print(color + goodjob, end='\x1b[2A'+'\r')
            time.sleep(0.03)
    print("\n\n")
    print(Fore.WHITE+"chroma: +30 000 pts")
    score+=50000
    chromasolved=True
    chromaread=True
    chromaprg_chance = 0
    file.remove("chroma")
    chromacode=0
    prgfound+=1
    
def readhex():
    global solvedall,score,prgfound,hexsolved
    hexes = []
    while True:
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
        print(Fore.GREEN,"\n*"+Fore.WHITE,"Type q to quit")
        print(Fore.GREEN,"\r*"+Fore.WHITE,"Enter here ",end="")
        while True:
            inp = input("> ")
            if inp == r:
                break
            else:
                print(Fore.RED,"\r*"+Fore.WHITE,"Wrong number ",end="")
            if inp == "q":
                break
            break
                
        print(Fore.YELLOW,"\r* Correct!")
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
            
        print(Fore.GREEN,"\r*"+Fore.WHITE,"Enter here ",end="")
        while True:
            inp = input("> ")
            if inp == r:
                break
            else:
                print(Fore.RED,"\r*"+Fore.WHITE,"Wrong number ",end="")
            if inp == "q":
                break
            break
                
        print(Fore.YELLOW,"\r* Correct!")
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
            
        print(Fore.GREEN,"\r*"+Fore.WHITE,"Enter here ",end="")
        while True:
            inp = input("> ")
            if inp == r:
                break
            else:
                print(Fore.RED,"\r*"+Fore.WHITE,"Wrong number ",end="")
            if inp == "q":
                break
            break
        
        print(Fore.YELLOW,"\r* Correct!")
        time.sleep(0.5)
        break
    print(Fore.WHITE,"\rhex: 100 000 pts")
    print('\n')
    hexsolved=True
    solvedall=True
    prgfound+=1
    print(Fore.YELLOW+Style.BRIGHT,"\r* All special programs found! +200 000 pts")
    file.remove("hex")
    
def gendirsback(x):
    global score,names_memory,names,memory,dir,file_memory,file,gendir,inemptydir
    if "empty" not in dir[x]:
        print(Fore.GREEN,"+100 pts")
        score+=100
        names_memory.clear()
        names_memory+=names
        names.clear()
        memory.clear()
        memory+=dir
        dir.clear()
        file_memory.clear()
        file_memory+=file
        file.clear()
        for i in range(len(memory[x])):
            print(Fore.BLUE+Style.BRIGHT,memory[x][i], end=" ")
            names.append(memory[x][i])
            for i in names:
                for i in range(random.randint(4,7)):
                    gendir.append(str(random.choice(dirs)))
                dir.append(list(gendir))
                gendir.clear()
    else:
        print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end=" ")
        inemptydir=True

def finallayer():
    global score,syntax,passwd,i
    screenwidth=os.get_terminal_size().columns
    screenheight=os.get_terminal_size().lines
    print(Fore.MAGENTA+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
    time.sleep(2)
    print(Fore.MAGENTA+Style.BRIGHT,"root",end=" ")
    print(Style.RESET_ALL)
    time.sleep(1)
    while True:
        syntax.clear()
        inp = input(str(username)+"@termadventure $ ")
        syntax = inp.split(" ")
        if inp == "cd root":
            if passwdfound==False:
                passwd = random.choice(rootpasswords)
                print(Style.DIM,"the password is "+str(passwd))
            prompt = input("* This directory is encrypted. Password? > ")        
            if prompt == str(passwd):
                break    
            else:
                prompt = input("* Incorrect password > ")
    passwd=0
    print("\n")
    chars=["/","@","#","$","%","&","*","!","?","^","~","`","-","_","=","+","|","{","}","[","]",":",";","<",">",",","."]
    for i in range(screenwidth//3):
        print(Fore.MAGENTA+Style.BRIGHT,3*i*str(random.choice(chars)))
        time.sleep(0.02)
    for i in range(300):
        print(Fore.MAGENTA+Style.BRIGHT,(screenwidth-1)*str(random.choice(chars)))
        time.sleep(0.02)
    for i in range(screenwidth//3):
        print(Fore.MAGENTA+Style.BRIGHT,(screenwidth-3*i)*str(random.choice(chars)))
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
    print(Fore.BLUE,"\r*"+Fore.WHITE,"Total points collected: "+str(score))
    time.sleep(2)
    if kernelsolved==True:
        print(Fore.BLUE+Style.BRIGHT,"\rkernelcode",end=" ")
    else:
        print(Fore.WHITE+Style.DIM,"\rkernelcode",end=" ")
    if chromasolved==True:
        for letter in ch:
            print(colors_map2.get(letter, Fore.WHITE) + letter, end='')
    else:
        print(Fore.WHITE+Style.DIM,"chroma",end=" ")
    if codexsolved==True:
        print(Fore.WHITE+Style.BRIGHT,"codex",end="")
    else:
        print(Fore.WHITE+Style.DIM,"codex",end="")
    if hexsolved==True:
        print(Fore.GREEN+Style.BRIGHT,"hex",end=" ")
    else:
        print(Fore.WHITE+Style.DIM,"hex",end=" ")
    if prgfound < 4:
        print(Fore.BLUE+Style.NORMAL,"\n* "+Fore.WHITE,str(prgfound)+"/4 special programs found")
    elif prgfound == 4:
        print(Fore.YELLOW+Style.NORMAL,"\n* "+str(prgfound)+"/4 special programs found")
    time.sleep(2)
    print(Style.RESET_ALL)
    inp = input("\r* Do you want to play again or quit the game? (y/n) ")
    if inp == "n":
        sys.exit()
    elif inp == "y":
        score = 0
         
# Core game                   
while True:
    memory=[]
    dir=[]
    names=[]
    names_memory=[]
    gendir=[]
    file=[]
    file_memory=[]
    readme=[]
    readme2=[]
    readme3=[]
    chromacode=0
    layer = 1
    codexprg_chance=0
    kernelcodeprg_chance=0
    chromaprg_chance=0
    hexprg_chance=0
    passwd_chance=0
    prgfound=0
    wentbackempty=False
    inemptydir=False
    kernelread=False
    codexread=False
    chromaread=False
    kernelsolved=False
    codexsolved=False
    chromasolved=False
    hexsolved=False
    solvedreadme=False
    solvedall=False
    passwdfound=False
    loading()
    print("\n"+Fore.BLUE+Style.NORMAL,"*"+Fore.WHITE,"Let's go!")
    time.sleep(2)
    print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
    
    print(Fore.BLUE+Style.BRIGHT,"home",end=" ")
    while True:
        print(Style.RESET_ALL)
        inp = input(str(username)+"@termadventure $ ")
        if inp == "cd home":
            break
        
        elif inp == "quit" or inp == "q":
            sys.exit()
            
        elif inp == "help":
            print("""
ls - list directories
cd (dir) - change directory
cd .. - leave the directory
cat (text file) - read the content of the text file
(executable) - run the program or claim bonus""")
        
    layer+=1
    score+=100
    print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer),end="  ")
    print(Fore.GREEN,"+100 pts")
    for i in range(random.randint(4,7)):
        names.append(str(random.choice(dirs)))
        print(Fore.BLUE+Style.BRIGHT,names[i],end=" ")
        
    for i in names:
        for i in range(random.randint(4,7)):
            gendir.append(str(random.choice(dirs)))
        dir.append(list(gendir))
        gendir.clear()
               
    while layer < 50:
        
        if inp == "cd .." and inemptydir == False and wentbackempty == False:
            print(Fore.YELLOW,"*"+Fore.WHITE,"Sorry, you can't go back",end=" ")
            
        if inp == "quit" or inp == "q":
            sys.exit()
            
        if inp == "help":
            print("""
ls - list directories
cd (dir) - change directory
cd .. - leave the directory
cat (text file) - read the content of the text file
(executable) - run the program or claim bonus""")
            
        if inp == "ls":
            if inemptydir==False:
                listfiles()
            elif inemptydir==True:
                print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end=" ")

        if inemptydir == True:
            print(Style.RESET_ALL)
            inp = input(str(username)+"@termadventure $ ")
            syntax = inp.split(" ")
            syntax+=[".."]
            
        if inp == "cd .." and inemptydir == True and wentbackempty == False: #cd .. when entered empty
            layer-=1
            print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
            listfiles()
            wentbackempty=True
            inemptydir=False

        if wentbackempty == False and inemptydir == False:
            print(Style.RESET_ALL)
            inp = input(str(username)+"@termadventure $ ")
            syntax = inp.split(" ")
            syntax+=[".."]
            
            if inp == str(syntax[0])+" "+str(syntax[1]):
                if syntax[1] in names: #cd dest
                    layer+=1
                    if layer == 50:
                        break
                    empty_chance = random.randint(1,10)
                    print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer),end="  ")
                    
                    if empty_chance < 9:
                        
                        print(Fore.GREEN,"+100 pts")
                        score+=100
                        memory.clear()
                        memory+=dir
                        names_memory.clear()
                        names_memory+=names
                        names.clear()
                        dir.clear()
                        file_memory.clear()
                        file_memory+=file
                        file.clear()
                        readme.clear()
                        readme2.clear()
                        readme3.clear()
                        bonus_chance = random.randint(1,15)
                        easter_chance = random.randint(1,15)
                        readme_chance = random.randint(1,15)
                        unknown_chance = random.randint(1,15)
                        genspecprogs()
                        
                        for i in range(len(names_memory)):
                            if syntax[1] == names_memory[i]:
                                gendirs(i)
                                break
                        genfiles()
                                    
                    elif empty_chance >= 9:
                        mkempty() 
                        inemptydir=True
                        print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end=" ")
                    
            if inp == files[0]:
                if inp == "bonus" and syntax[0] in file: #bonus
                    bonusscore = random.choice(bonuses)
                    print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                    score+=bonusscore
                    file.remove("bonus")
                        
            if inp == files[1]:
                if inp == "easteregg" and syntax[0] in file: #easteregg
                    print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10 000 pts",end=" ")
                    score+=10000
                    file.remove("easteregg")
                    
            if inp == "cat "+str(files[2]):
                if files[2] in file:  #readme files
                    readfile1()
                        
            if inp == "cat "+str(files[3]):
                if files[3] in file:
                    readfile2()
                        
            if inp == "cat "+str(files[4]):
                if files[4] in file:
                    readfile3()

            if inp == files[5]:
                crash_chance = random.randint(1,15)
                bonus_chance = random.randint(1,15)
                if inp == "unknown" and syntax[0] in file:
                    wait = time.time() + 0.5
                    while time.time() < wait:
                        print(".",end="", flush=True)
                        time.sleep(0.003)
                    if crash_chance < 13:
                        if bonus_chance >= 14:
                            print("\n")
                            bonusscore = random.choice(bonuses)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                            score+=bonusscore
                            file.remove("unknown")
                                
                        elif bonus_chance < 14:
                            file.remove("unknown")
                            
                    elif crash_chance > 13:
                        crash()
                        inp = input("\r* Do you want to play again or quit the game? (y/n) ")
                        if inp == "n":
                            sys.exit()
                        elif inp == "y":
                            score = 0
                            layer=0
                            break
                        
            if inp == files[6]:
                if files[6] in file:
                    readlorem()
            if inp == files[7]:
                if files[7] in file:
                    readkernel()
            if inp == files[8]:
                if files[8] in file:
                    readchroma()
            if inp == files[9]:
                if files[9] in file:
                    readhex()
            
        if wentbackempty == True and inemptydir == False:
            print(Style.RESET_ALL)
            inp = input(str(username)+"@termadventure $ ")
            syntax = inp.split(" ")
            syntax+=[".."]
            
            if inp == str(syntax[0])+" "+str(syntax[1]):  
                if syntax[0] == "cd" and syntax[1] in names: #cd (newdest)
                    
                    if syntax[1] in names: #cd dest
                        layer+=1
                        empty_chance = random.randint(1,10)
                        bonus_chance = random.randint(1,15)
                        easter_chance = random.randint(1,15)
                        readme_chance = random.randint(1,15)
                        unknown_chance = random.randint(1,15)
                        genspecprogs()
                            
                        print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer),end="  ")
                        if empty_chance < 9:
                            for i in range(len(names)):
                                if syntax[1] == names[i]:
                                    gendirsback(i)
                                    break
                            if inemptydir == False:
                                genfiles()
                        
                        elif empty_chance >= 9:
                            mkempty()
                            inemptydir=True
                            print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end=" ")
                        wentbackempty=False
                        
                if inp == "cd .." and wentbackempty == True:
                    print(Fore.YELLOW,"*"+Fore.WHITE,"You can't go back now!",end=" ")
                    
            if inp == "cat "+str(files[2]):
                if files[2] in file:  #readme files
                    readfile1()
            if inp == "cat "+str(files[3]):
                if files[3] in file:
                    readfile2()
            if inp == "cat "+str(files[4]):
                if files[4] in file:
                    readfile3()
                    
            if inp == files[5]:
                crash_chance = random.randint(1,15)
                bonus_chance = random.randint(1,15)
                if inp == "unknown" and syntax[0] in file:
                    wait = time.time() + 0.5
                    while time.time() < wait:
                        print(".",end="", flush=True)
                        time.sleep(0.003)
                    if crash_chance < 10:
                        if bonus_chance >= 14:
                            print("\n")
                            bonusscore = random.choice(bonuses)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                            score+=bonusscore
                            file.remove("unknown")
                                
                        elif bonus_chance < 14:
                            file.remove("unknown")
                            
                    elif crash_chance > 10:
                        crash()
                        inp = input("\r* Do you want to play again or quit the game? (y/n) ")
                        if inp == "n":
                            sys.exit()
                        elif inp == "y":
                            score = 0
                            layer=0
                            break
                            
            if inp == files[6]:           
                if files[6] in file:
                    readlorem()
            if inp == files[7]:
                if files[7] in file:
                    readkernel()
            if inp == files[8]:
                if files[8] in file:
                    readchroma()
            if inp == files[9]:
                if files[9] in file:
                    readhex()
                    
            if inp == "bonus" and syntax[0] in file: #bonus
                    bonusscore = random.choice(bonuses)
                    print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                    score+=bonusscore
                    file.remove("bonus")
                        
            if syntax[0] == "easteregg" and syntax[0] in file: #easteregg
                print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10 000 pts",end=" ")
                score+=10000
                file.remove("easteregg")

    if layer == 50:
        finallayer()