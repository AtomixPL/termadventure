# elements.py
# TermAdventure elements functions
# Copyright (c) 2025 AtomixPL
# Licensed under the GNU General Public License

import time
import random

from colorama import Fore, Style
from dynamic.dynamic import d
from constants.constants import c

class Elements: 
    def listfiles(self):
        for i in range(len(d.names)):
            print(Fore.BLUE+Style.BRIGHT,d.names[i],end=" ")
        if "bonus" in d.file:
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[0],end=" ")
        if "codex" in d.file:
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[6],end=" ")
        if "kernelcode" in d.file:
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[7],end=" ")
        if "chroma" in d.file:
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[8],end=" ")
        if "hex" in d.file:
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[9],end=" ")
        if "easteregg" in d.file:
            print(Fore.YELLOW+Style.BRIGHT,c.files[1],end=" ")
        if "unknown" in d.file:
            print(Fore.RED+Style.BRIGHT,c.files[5],end=" ")
        if "readme" in d.file:
            print(Fore.WHITE+Style.NORMAL,c.files[2],end=" ")
        if "d.readme2" in d.file:
            print(Fore.WHITE+Style.NORMAL,c.files[3],end=" ")
        if "d.readme3" in d.file:
            print(Fore.WHITE+Style.NORMAL,c.files[4],end=" ")
    
    def genspecprogs(self): # If readme of program found then generate the program 
        if d.codexread==True and d.codexsolved==False:
            d.codexprg_chance = random.randint(1,20)
        if d.kernelread==True and d.kernelsolved==False:
            d.kernelcodeprg_chance = random.randint(1,20)
        if d.chromaread==True and d.chromasolved==False:
            d.chromaprg_chance = random.randint(1,20)
        if d.codexsolved==True and d.hexsolved==False:
            d.hexprg_chance = random.randint(1,20)
        
    def gendirs(self,x): # If names[x] picked then move dir list contents to memory, print memory[x], for every memory[x] directory generate new content for new names[x]
        for i in range(len(d.memory[x])):
            print(Fore.BLUE+Style.BRIGHT,d.memory[x][i],end=" ")
            d.names.append(d.memory[x][i])
        for i in d.memory[x]:
            for i in range(random.randint(4,7)):
                d.gendir.append(str(random.choice(c.dirs)))
            d.dir.append(list(d.gendir))
            d.gendir.clear()

    def genfiles(self): # Generate executables and readme files
        if d.bonus_chance > 8:
            d.file.append(str(c.files[0]))
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[0],end=" ")
        if d.codexprg_chance >= 16:
            d.file.append(str(c.files[6]))
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[6],end=" ")
        if d.kernelcodeprg_chance >= 16:
            d.file.append(str(c.files[7]))
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[7],end=" ")
        if d.chromaprg_chance >= 16:
            d.file.append(str(c.files[8]))
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[8],end=" ")
        if d.hexprg_chance >= 18:
            if d.hexsolved == False and d.solvedall == False:
                d.file.append(str(c.files[9]))
                print(Fore.LIGHTGREEN_EX+Style.BRIGHT,c.files[9],end=" ")
        if d.easter_chance > 14:
            d.file.append(str(c.files[1]))
            print(Fore.YELLOW+Style.BRIGHT,c.files[1],end=" ")                      
        if d.unknown_chance > 10:
            d.file.append(str(c.files[5]))
            print(Fore.RED+Style.BRIGHT,c.files[5],end=" ")
        if d.readme_chance > 7:
            readmenum = random.randint(1,3)
            if readmenum == 1:
                d.file.append(str(c.files[2]))
                print(Fore.WHITE+Style.NORMAL,c.files[2],end=" ")   
            elif readmenum == 2:
                d.file.append(str(c.files[2]))
                d.file.append(str(c.files[3]))
                print(Fore.WHITE+Style.NORMAL,c.files[2],end=" ")
                print(Fore.WHITE+Style.NORMAL,c.files[3],end=" ")
            elif readmenum == 3:
                d.file.append(str(c.files[2]))
                d.file.append(str(c.files[3]))
                d.file.append(str(c.files[4]))
                print(Fore.WHITE+Style.NORMAL,c.files[2],end=" ")
                print(Fore.WHITE+Style.NORMAL,c.files[3],end=" ")
                print(Fore.WHITE+Style.NORMAL,c.files[4],end=" ")     

    def mkempty(self):
        if d.syntax[1] == d.names[0]:
            d.dir[0].append("empty")
        elif d.syntax[1] == d.names[1]:
            d.dir[1].append("empty")
        elif d.syntax[1] == d.names[2]:
            d.dir[2].append("empty")
        elif d.syntax[1] == d.names[3]:
            d.dir[3].append("empty")
        elif d.syntax[1] == d.names[4]:
            d.dir[4].append("empty")
        elif d.syntax[1] == d.names[5]:
            d.dir[5].append("empty")
        elif d.syntax[1] == d.names[6]:
            d.dir[6].append("empty")
            
    def readfile1(self):
        if not d.readme:
            if d.kernelread==False:
                d.kernelcode_chance = random.randint(1,40)
            if d.codexread==False:
                d.codex_chance = random.randint(1,40) 
            if d.chromaread==False:
                d.chroma_chance = random.randint(1,40)
            d.bonus_chance = random.randint(1,20)
            readmescore = random.randint(1,20)
            d.passwd_chance = random.randint(1,40)
            
            if d.kernelcode_chance >= 33 and d.kernelsolved==False and d.kernelread==False:
                if d.kernelread == False:
                    print(c.specialreadmetexts[0],end=" ")
                    d.kernelcode=random.randint(111,999)
                    print(d.kernelcode,end="")
                    d.readme.append(str(c.specialreadmetexts[0])+" "+str(d.kernelcode))
                    d.kernelread=True
                    d.kernelcode_chance = 0
                    
            elif d.codex_chance >= 33 and d.codexsolved==False and d.codexread==False and d.kernelsolved==True and d.chromasolved==True:
                if d.codexread == False:
                    codex = dict(random.sample(list(c.latinnums.items()), 3))
                    print(c.specialreadmetexts[1])
                    print(*codex.keys(), end="")
                    d.readme.append(str(c.specialreadmetexts[1]))
                    d.readme.append("".join(codex.keys()))
                    d.codexnum = list(codex.values())
                    d.codexread=True
                    d.codex_chance = 0
                    
            elif d.chroma_chance >= 33 and d.chromasolved==False and d.chromaread==False and d.kernelsolved==True:
                if d.chromaread == False:
                    chroma = random.sample(c.colors,len(c.colors))
                    for i in range(len(chroma)):
                        color = c.colors_map.get(chroma[i], Fore.WHITE)
                        print(color + chroma[i], end='')
                    d.readme.append(''.join(chroma))
                    d.chromacode = ''.join(chroma)
                    d.chromaread=True
                    d.chroma_chance = 0
                    
            elif d.passwd_chance >= 37 and d.passwdfound == False:
                c.passwd = random.choice(c.rootpasswords)
                d.readme.append(c.specialreadmetexts[4]+str(c.passwd))
                print(*d.readme,end="")
                d.passwdfound=True
                            
            elif d.bonus_chance == 20:
                bonusscore = random.choice(c.bonuses)
                print(c.specialreadmetexts[2],end="")
                print(bonusscore)
                print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                d.score+=bonusscore
                d.readme.append(str(c.specialreadmetexts[2]+str(bonusscore)))
                
            elif readmescore == 20:
                d.readme.append(c.specialreadmetexts[3]+str(d.score))
                print(*d.readme,end="")
                
            else:
                d.readme.append(str(random.choice(c.readmetexts)))
                print(*d.readme,end="\r")
        else:
            if d.chromacode != 0:
                for i in range(len(chroma)):
                        color = c.colors_map.get(chroma[i], Fore.WHITE)
                        print(color + chroma[i], end='')
            else: 
                print(*d.readme,end="\r")
                
    def readfile2(self):
        if not d.readme2:
            if d.kernelread==False:
                d.kernelcode_chance = random.randint(1,20)
            if d.codexread==False:
                d.codex_chance = random.randint(1,30) 
            if d.chromaread==False:
                d.chroma_chance = random.randint(1,40)
            d.bonus_chance = random.randint(1,20)
            readmescore = random.randint(1,20)
            d.passwd_chance = random.randint(1,40)
            
            if d.kernelcode_chance >= 33 and d.kernelsolved==False and d.kernelread==False:
                if d.kernelread == False:
                    print(c.specialreadmetexts[0],end=" ")
                    d.kernelcode=random.randint(111,999)
                    print(d.kernelcode,end="")
                    d.readme2.append(str(c.specialreadmetexts[0])+" "+str(d.kernelcode))
                    d.kernelread=True
                    d.kernelcode_chance = 0
                    
            elif d.codex_chance >= 33 and d.codexsolved==False and d.codexread==False and d.kernelsolved==True and d.chromasolved==True:
                if d.codexread == False:
                    codex = dict(random.sample(list(c.latinnums.items()), 3))
                    print(c.specialreadmetexts[1])
                    print(*codex.keys(), end="")
                    d.readme2.append(str(c.specialreadmetexts[1]))
                    d.readme2.append("".join(codex.keys()))
                    d.codexnum = list(codex.values())
                    d.codexread=True
                    d.codex_chance = 0
            
            elif d.chroma_chance >= 33 and d.chromasolved==False and d.chromaread==False and d.kernelsolved==True:
                if d.chromaread == False:
                    chroma = random.sample(c.colors,len(c.colors))
                    for i in range(len(chroma)):
                        color = c.colors_map.get(chroma[i], Fore.WHITE)
                        print(color + chroma[i], end='')
                    print(Style.RESET_ALL)
                    d.readme2.append(''.join(chroma))
                    d.chromacode = ''.join(chroma)
                    d.chromaread=True
                    d.chroma_chance = 0
                    
            elif d.passwd_chance >= 37 and d.passwdfound == False:
                c.passwd = random.choice(c.rootpasswords)
                d.readme2.append(c.specialreadmetexts[4]+str(c.passwd))
                print(*d.readme2,end="")
                d.passwdfound=True
            
            elif d.bonus_chance == 20:
                bonusscore = random.choice(c.bonuses)
                print(c.specialreadmetexts[2],end="")
                print(bonusscore)
                print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                d.score+=bonusscore
                d.readme2.append(str(c.specialreadmetexts[2]+str(bonusscore)))
            
            elif readmescore == 20:
                d.readme2.append(c.specialreadmetexts[3]+str(d.score))
                print(*d.readme2,end="")
            
            else:
                d.readme2.append(str(random.choice(c.readmetexts)))
                print(*d.readme2,end="\r")
        else:
            if d.chromacode != 0:
                for i in range(len(chroma)):
                        color = c.colors_map.get(chroma[i], Fore.WHITE)
                        print(color + chroma[i], end='')
            else: 
                print(*d.readme2,end="\r")
                
    def readfile3(self):
        if not d.readme3:
            if d.kernelread==False:
                d.kernelcode_chance = random.randint(1,20)
            if d.codexread==False:
                d.codex_chance = random.randint(1,30) 
            if d.chromaread==False:
                d.chroma_chance = random.randint(1,40)
            d.bonus_chance = random.randint(1,20)
            readmescore = random.randint(1,20)
            d.passwd_chance = random.randint(1,40)
            
            if d.kernelcode_chance >= 33 and d.kernelsolved==False and d.kernelread==False:
                if d.kernelread == False:
                    print(c.specialreadmetexts[0],end=" ")
                    d.kernelcode=random.randint(111,999)
                    print(d.kernelcode,end="")
                    d.readme3.append(str(c.specialreadmetexts[0])+" "+str(d.kernelcode))
                    d.kernelread=True
                    d.kernelcode_chance = 0
                    
            elif d.codex_chance >= 33 and d.codexsolved==False and d.codexread==False and d.kernelsolved==True and d.chromasolved==True:
                if d.codexread == False:
                    codex = dict(random.sample(list(c.latinnums.items()), 3))
                    print(c.specialreadmetexts[1])
                    print(*codex.keys(), end="")
                    d.readme3.append(str(c.specialreadmetexts[1]))
                    d.readme3.append("".join(codex.keys()))
                    d.codexnum = list(codex.values())
                    d.codexread=True
                    d.codex_chance = 0
                
            elif d.chroma_chance >= 33 and d.chromasolved==False and d.chromaread==False and d.kernelsolved==True:
                if d.chromaread == False:
                    chroma = random.sample(c.colors,len(c.colors))
                    for i in range(len(chroma)):
                        color = c.colors_map.get(chroma[i], Fore.WHITE)
                        print(color + chroma[i], end='')
                    print(Style.RESET_ALL)
                    d.readme3.append(''.join(chroma))
                    d.chromacode = ''.join(chroma)
                    d.chromaread=True
                    d.chroma_chance = 0
                    
            elif d.passwd_chance >= 37 and d.passwdfound == False:
                c.passwd = random.choice(c.rootpasswords)
                d.readme3.append(c.specialreadmetexts[4]+str(c.passwd))
                print(*d.readme3,end="")
                d.passwdfound=True
            
            elif d.bonus_chance == 20:
                bonusscore = random.choice(c.bonuses)
                print(c.specialreadmetexts[2],end="")
                print(bonusscore)
                print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end=" ")
                d.score+=bonusscore
                d.readme3.append(str(c.specialreadmetexts[2]+str(bonusscore)))
            
            elif readmescore == 20:
                d.readme3.append(c.specialreadmetexts[3]+str(d.score))
                print(*d.readme3,end="")
                
            else:
                d.readme3.append(str(random.choice(c.readmetexts)))
                print(*d.readme3,end="\r")
        else:
            if d.chromacode != 0:
                for i in range(len(chroma)):
                        color = c.colors_map.get(chroma[i], Fore.WHITE)
                        print(color + chroma[i], end='')
            else: 
                print(*d.readme3,end="\r")
        
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
        print("codex: +50 000 pts")
        d.score+=30000
        d.codexsolved=True
        d.codexread=True
        d.codexprg_chance = 0
        d.file.remove("codex")
        d.prgfound+=1

    def readkernel(self):
        print(Fore.WHITE,"-= Kernel code check ",end="")
        while True:
            inp = input("> ")
            if inp == str(d.kernelcode):
                break
            else:
                print(Fore.WHITE,"-= Incorrect code ",end="")
        print("kernelcode: +20 000 pts")
        d.score+=20000
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
        print(Fore.WHITE,"\rEnter code: ",end="")
        while True:
            inp = input("=> ")
            if inp == str(d.chromacode):
                break
            else:
                print(Fore.WHITE,"\rIncorrect code ",end="")
        for i in range(3):
            for color in c.coloramas:
                print(color + c.chromagj, end='\x1b[2A'+'\r')
                time.sleep(0.03)
        print("\n\n")
        print(Fore.WHITE+"chroma: +30 000 pts")
        d.score+=50000
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
        print(Fore.WHITE,"\rhex: 100 000 pts")
        print('\n')
        d.score+=100000
        d.hexsolved=True
        d.solvedall=True
        d.prgfound+=1
        print(Fore.YELLOW+Style.BRIGHT,"\r* All special programs found! +200 000 pts")
        d.score+=200000
        d.file.remove("hex")
        
    def gendirsback(self,x): # Generate dirs if player is behind one directory
        if "empty" not in d.dir[x]:
            print(Fore.GREEN,"+100 pts")
            d.score+=100
            d.names_memory.clear()
            d.names_memory+=d.names
            d.names.clear()
            d.memory.clear()
            d.memory+=d.dir
            d.dir.clear()
            d.file_memory.clear()
            d.file_memory+=d.file
            d.file.clear()
            for i in range(len(d.memory[x])):
                print(Fore.BLUE+Style.BRIGHT,d.memory[x][i], end=" ")
                d.names.append(d.memory[x][i])
                for i in d.names:
                    for i in range(random.randint(4,7)):
                        d.gendir.append(str(random.choice(c.dirs)))
                    d.dir.append(list(d.gendir))
                    d.gendir.clear()
        else:
            print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end=" ")
            d.inemptydir=True
            
e = Elements()