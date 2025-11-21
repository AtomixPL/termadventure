# termadventure.py
# Copyright (c) 2025 AtomixPL
# Licensed under the GNU General Public License

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
    
from var.const_vars import c

score = 0
print(Fore.BLUE+Style.BRIGHT+c.logo, end="") # Print menu
print(Fore.WHITE,"Copyright (c) 2025 AtomixPL"+Style.NORMAL,"                                      v1.0.4")
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
        username = inp.lower()
        break

def loading(): # Loading simulation
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
    global names,file
    for i in range(len(names)):
        print(Fore.BLUE+Style.BRIGHT,names[i],end=" ")
    if "bonus" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[0],end=" ")
    if "codex" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[6],end=" ")
    if "kernelcode" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[7],end=" ")
    if "chroma" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[8],end=" ")
    if "hex" in file:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[9],end=" ")
    if "easteregg" in file:
        print(Fore.YELLOW+Style.BRIGHT,c.files[1],end=" ")
    if "unknown" in file:
        print(Fore.RED+Style.BRIGHT,c.files[5],end=" ")
    if "readme" in file:
        print(Fore.WHITE+Style.NORMAL,c.files[2],end=" ")
    if "readme2" in file:
        print(Fore.WHITE+Style.NORMAL,c.files[3],end=" ")
    if "readme3" in file:
        print(Fore.WHITE+Style.NORMAL,c.files[4],end=" ")
    
def genspecprogs(): # If readme of program found then generate the program 
    global codexprg_chance,kernelcodeprg_chance,chromaprg_chance,codexsolved,hexprg_chance
    if codexread==True and codexsolved==False:
        codexprg_chance = random.randint(1,20)
    if kernelread==True and kernelsolved==False:
        kernelcodeprg_chance = random.randint(1,20)
    if chromaread==True and chromasolved==False:
        chromaprg_chance = random.randint(1,20)
    if codexsolved==True and hexsolved==False:
        hexprg_chance = random.randint(1,20)
    
def gendirs(x): # If names[x] picked then move dir list contents to memory, print memory[x], for every memory[x] directory generate new content for new names[x]
    global memory,names,gendir,dir
    for i in range(len(memory[x])):
        print(Fore.BLUE+Style.BRIGHT,memory[x][i],end=" ")
        names.append(memory[x][i])
    for i in memory[x]:
        for i in range(random.randint(4,7)):
            gendir.append(str(random.choice(c.dirs)))
        dir.append(list(gendir))
        gendir.clear()

def genfiles(): # Generate executables and readme files
    if bonus_chance > 8:
        file.append(str(c.files[0]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[0],end=" ")
    if codexprg_chance >= 16:
        file.append(str(c.files[6]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[6],end=" ")
    if kernelcodeprg_chance >= 16:
        file.append(str(c.files[7]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[7],end=" ")
    if chromaprg_chance >= 16:
        file.append(str(c.files[8]))
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[8],end=" ")
    if hexprg_chance >= 18:
        if hexsolved == False and solvedall == False:
            file.append(str(c.files[9]))
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[9],end=" ")
    if easter_chance > 14:
        file.append(str(c.files[1]))
        print(Fore.YELLOW+Style.BRIGHT,c.files[1],end=" ")                      
    if unknown_chance > 10:
        file.append(str(c.files[5]))
        print(Fore.RED+Style.BRIGHT,c.files[5],end=" ")
    if readme_chance > 7:
        readmenum = random.randint(1,3)
        if readmenum == 1:
            file.append(str(c.files[2]))
            print(Fore.WHITE+Style.NORMAL,c.files[2],end=" ")   
        elif readmenum == 2:
            file.append(str(c.files[2]))
            file.append(str(c.files[3]))
            print(Fore.WHITE+Style.NORMAL,c.files[2],end=" ")
            print(Fore.WHITE+Style.NORMAL,c.files[3],end=" ")
        elif readmenum == 3:
            file.append(str(c.files[2]))
            file.append(str(c.files[3]))
            file.append(str(c.files[4]))
            print(Fore.WHITE+Style.NORMAL,c.files[2],end=" ")
            print(Fore.WHITE+Style.NORMAL,c.files[3],end=" ")
            print(Fore.WHITE+Style.NORMAL,c.files[4],end=" ")     

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
                print(c.specialreadmetexts[0],end=" ")
                kernelcode=random.randint(111,999)
                print(kernelcode,end="")
                readme.append(str(c.specialreadmetexts[0])+" "+str(kernelcode))
                kernelread=True
                kernelcode_chance = 0
                
        elif codex_chance >= 33 and codexsolved==False and codexread==False and kernelsolved==True and chromasolved==True:
            if codexread == False:
                codex = dict(random.sample(list(c.latinnums.items()), 3))
                print(c.specialreadmetexts[1])
                print(*codex.keys(), end="")
                readme.append(str(c.specialreadmetexts[1]))
                readme.append("".join(codex.keys()))
                codexnum = list(codex.values())
                codexread=True
                codex_chance = 0
                
        elif chroma_chance >= 33 and chromasolved==False and chromaread==False and kernelsolved==True:
            if chromaread == False:
                chroma = random.sample(c.colors,len(c.colors))
                for i in range(len(chroma)):
                    color = c.colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
                readme.append(''.join(chroma))
                chromacode = ''.join(chroma)
                chromaread=True
                chroma_chance = 0
                
        elif passwd_chance >= 37 and passwdfound == False:
            passwd = random.choice(c.rootpasswords)
            readme.append(c.specialreadmetexts[4]+str(passwd))
            print(*readme,end="")
            passwdfound=True
                        
        elif bonus_chance == 20:
            bonusscore = random.choice(c.bonuses)
            print(c.specialreadmetexts[2],end="")
            print(bonusscore)
            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
            score+=bonusscore
            readme.append(str(c.specialreadmetexts[2]+str(bonusscore)))
            
        elif readmescore == 20:
            readme.append(c.specialreadmetexts[3]+str(score))
            print(*readme,end="")
            
        elif kernelcode_chance  < 33 or codex_chance < 33 or chroma_chance < 33 or passwd_chance < 37 or bonus_chance != 20 or readmescore != 20 or kernelsolved == True or codexsolved == True:
            readme.append(str(random.choice(c.readmetexts)))
            print(*readme,end="\r")
    else:
        if chromacode != 0:
            for i in range(len(chroma)):
                    color = c.colors_map.get(chroma[i], Fore.WHITE)
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
                print(c.specialreadmetexts[0],end=" ")
                kernelcode=random.randint(111,999)
                print(kernelcode,end="")
                readme2.append(str(c.specialreadmetexts[0])+" "+str(kernelcode))
                kernelread=True
                kernelcode_chance = 0
                
        elif codex_chance >= 33 and codexsolved==False and codexread==False and kernelsolved==True and chromasolved==True:
            if codexread == False:
                codex = dict(random.sample(list(c.latinnums.items()), 3))
                print(c.specialreadmetexts[1])
                print(*codex.keys(), end="")
                readme2.append(str(c.specialreadmetexts[1]))
                readme2.append("".join(codex.keys()))
                codexnum = list(codex.values())
                codexread=True
                codex_chance = 0
        
        elif chroma_chance >= 33 and chromasolved==False and chromaread==False and kernelsolved==True:
            if chromaread == False:
                chroma = random.sample(c.colors,len(c.colors))
                for i in range(len(chroma)):
                    color = c.colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
                print(Style.RESET_ALL)
                readme2.append(''.join(chroma))
                chromacode = ''.join(chroma)
                chromaread=True
                chroma_chance = 0
                
        elif passwd_chance >= 37 and passwdfound == False:
            passwd = random.choice(c.rootpasswords)
            readme2.append(c.specialreadmetexts[4]+str(passwd))
            print(*readme2,end="")
            passwdfound=True
        
        elif bonus_chance == 20:
            bonusscore = random.choice(c.bonuses)
            print(c.specialreadmetexts[2],end="")
            print(bonusscore)
            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
            score+=bonusscore
            readme2.append(str(c.specialreadmetexts[2]+str(bonusscore)))
        
        elif readmescore == 20:
            readme2.append(c.specialreadmetexts[3]+str(score))
            print(*readme2,end="")
        
        elif kernelcode_chance  < 33 or codex_chance < 33 or chroma_chance < 33 or passwd_chance < 37 or bonus_chance != 20 or readmescore != 20 or kernelsolved == True or codexsolved == True:
            readme2.append(str(random.choice(c.readmetexts)))
            print(*readme2,end="\r")
    else:
        if chromacode != 0:
            for i in range(len(chroma)):
                    color = c.colors_map.get(chroma[i], Fore.WHITE)
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
                print(c.specialreadmetexts[0],end=" ")
                kernelcode=random.randint(111,999)
                print(kernelcode,end="")
                readme3.append(str(c.specialreadmetexts[0])+" "+str(kernelcode))
                kernelread=True
                kernelcode_chance = 0
                
        elif codex_chance >= 33 and codexsolved==False and codexread==False and kernelsolved==True and chromasolved==True:
            if codexread == False:
                codex = dict(random.sample(list(c.latinnums.items()), 3))
                print(c.specialreadmetexts[1])
                print(*codex.keys(), end="")
                readme3.append(str(c.specialreadmetexts[1]))
                readme3.append("".join(codex.keys()))
                codexnum = list(codex.values())
                codexread=True
                codex_chance = 0
            
        elif chroma_chance >= 33 and chromasolved==False and chromaread==False and kernelsolved==True:
            if chromaread == False:
                chroma = random.sample(c.colors,len(c.colors))
                for i in range(len(chroma)):
                    color = c.colors_map.get(chroma[i], Fore.WHITE)
                    print(color + chroma[i], end='')
                print(Style.RESET_ALL)
                readme3.append(''.join(chroma))
                chromacode = ''.join(chroma)
                chromaread=True
                chroma_chance = 0
                
        elif passwd_chance >= 37 and passwdfound == False:
            passwd = random.choice(c.rootpasswords)
            readme3.append(c.specialreadmetexts[4]+str(passwd))
            print(*readme3,end="")
            passwdfound=True
        
        elif bonus_chance == 20:
            bonusscore = random.choice(c.bonuses)
            print(c.specialreadmetexts[2],end="")
            print(bonusscore)
            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
            score+=bonusscore
            readme3.append(str(c.specialreadmetexts[2]+str(bonusscore)))
        
        elif readmescore == 20:
            readme3.append(c.specialreadmetexts[3]+str(score))
            print(*readme3,end="")
            
        elif kernelcode_chance  < 33 or codex_chance < 33 or chroma_chance < 33 or passwd_chance < 37 or bonus_chance != 20 or readmescore != 20 or kernelsolved == True or codexsolved == True:
            readme3.append(str(random.choice(c.readmetexts)))
            print(*readme3,end="\r")
    else:
        if chromacode != 0:
            for i in range(len(chroma)):
                    color = c.colors_map.get(chroma[i], Fore.WHITE)
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
        for letter in c.ch:
            print(c.colors_map2.get(letter, Fore.WHITE) + letter, end='')
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
    print(c.codexgreeter)
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
    for color in c.coloramas:
        print(color + c.chromagreeter, end='\x1b[2A'+'\r')
        time.sleep(0.1)
    print("\n\n")
    print(Fore.WHITE,"\rEnter code: ",end="")
    while True:
        inp = input("=> ")
        if inp == str(chromacode):
            break
        else:
            print(Fore.WHITE,"\rIncorrect code ",end="")
    for i in range(3):
        for color in c.coloramas:
            print(color + c.chromagj, end='\x1b[2A'+'\r')
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
        
    print(Fore.GREEN,"\r*"+Fore.WHITE,"Enter here ",end="")
    while True:
        inp = input("> ")
        if inp == r:
            break
        elif inp != r:
            print(Fore.RED,"\r*"+Fore.WHITE,"Wrong number ",end="")
    
    print(Fore.YELLOW,"\n* Correct!")
    time.sleep(0.5)
    print(Fore.WHITE,"\rhex: 100 000 pts")
    print('\n')
    hexsolved=True
    solvedall=True
    prgfound+=1
    print(Fore.YELLOW+Style.BRIGHT,"\r* All special programs found! +200 000 pts")
    file.remove("hex")
    
def gendirsback(x): # Generate dirs if player is behind one directory
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
                    gendir.append(str(random.choice(c.dirs)))
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
                passwd = random.choice(c.rootpasswords)
                print(Style.DIM,"* the password is "+str(passwd))
                print(Style.RESET_ALL)
            prompt = input("* This directory is encrypted. Password? > ")        
            if prompt == str(passwd):
                break    
            else:
                prompt = input("* Incorrect password > ")
    passwd=0
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
    print(Fore.BLUE,"\r*"+Fore.WHITE,"Total points collected: "+str(score))
    time.sleep(2)
    if kernelsolved==True:
        print(Fore.BLUE+Style.BRIGHT,"\rkernelcode",end=" ")
    else:
        print(Fore.WHITE+Style.DIM,"\rkernelcode",end=" ")
    if chromasolved==True:
        for letter in c.ch:
            print(c.colors_map2.get(letter, Fore.WHITE) + letter, end='')
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
            print(c.help)
        
    layer+=1
    score+=100
    print(Fore.BLUE+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer),end="  ")
    print(Fore.GREEN,"+100 pts")
    for i in range(random.randint(4,7)):
        names.append(str(random.choice(c.dirs)))
        print(Fore.BLUE+Style.BRIGHT,names[i],end=" ")
        
    for i in names:
        for i in range(random.randint(4,7)):
            gendir.append(str(random.choice(c.dirs)))
        dir.append(list(gendir))
        gendir.clear()
               
    while layer < 50:
        
        if inp == "cd .." and inemptydir == False and wentbackempty == False:
            print(Fore.YELLOW,"*"+Fore.WHITE,"Sorry, you can't go back",end=" ")
            
        if inp == "quit" or inp == "q":
            sys.exit()
            
        if inp == "help":
            print(c.help)
            
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
                    
            if inp == c.files[0]:
                if inp == "bonus" and syntax[0] in file: #bonus
                    bonusscore = random.choice(c.bonuses)
                    print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                    score+=bonusscore
                    file.remove("bonus")
                        
            if inp == c.files[1]:
                if inp == "easteregg" and syntax[0] in file: #easteregg
                    print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10 000 pts",end=" ")
                    score+=10000
                    file.remove("easteregg")
                    
            if inp == "cat "+str(c.files[2]):
                if c.files[2] in file:  #readme files
                    readfile1()
                        
            if inp == "cat "+str(c.files[3]):
                if c.files[3] in file:
                    readfile2()
                        
            if inp == "cat "+str(c.files[4]):
                if c.files[4] in file:
                    readfile3()

            if inp == c.files[5]:
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
                            bonusscore = random.choice(c.bonuses)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                            score+=bonusscore
                            file.remove("unknown")
                                
                        elif bonus_chance < 14:
                            file.remove("unknown")
                            
                    elif crash_chance > 13:
                        crash()
                        print(Style.RESET_ALL)
                        inp = input("\r* Do you want to play again or quit the game? (y/n) ")
                        if inp == "n":
                            sys.exit()
                        elif inp == "y":
                            score = 0
                            layer=0
                            break
                        
            if inp == c.files[6]:
                if c.files[6] in file:
                    readlorem()
            if inp == c.files[7]:
                if c.files[7] in file:
                    readkernel()
            if inp == c.files[8]:
                if c.files[8] in file:
                    readchroma()
            if inp == c.files[9]:
                if c.files[9] in file:
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
                    
            if inp == "cat "+str(c.files[2]):
                if c.files[2] in file:  #readme files
                    readfile1()
            if inp == "cat "+str(c.files[3]):
                if c.files[3] in file:
                    readfile2()
            if inp == "cat "+str(c.files[4]):
                if c.files[4] in file:
                    readfile3()
                    
            if inp == c.files[5]:
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
                            bonusscore = random.choice(c.bonuses)
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
                            
            if inp == c.files[6]:           
                if c.files[6] in file:
                    readlorem()
            if inp == c.files[7]:
                if c.files[7] in file:
                    readkernel()
            if inp == c.files[8]:
                if c.files[8] in file:
                    readchroma()
            if inp == c.files[9]:
                if c.files[9] in file:
                    readhex()
                    
            if inp == "bonus" and syntax[0] in file: #bonus
                    bonusscore = random.choice(c.bonuses)
                    print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                    score+=bonusscore
                    file.remove("bonus")
                        
            if syntax[0] == "easteregg" and syntax[0] in file: #easteregg
                print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10 000 pts",end=" ")
                score+=10000
                file.remove("easteregg")

    if layer == 50:
        finallayer()