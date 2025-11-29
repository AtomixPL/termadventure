# termadvfiles.py
# TermAdventure in-game files and directories functions
# Copyright (c) 2025 Atomix
# Licensed under the GNU General Public License

import random

from colorama import Fore, Style
from dynvars import d
from constvars import c

class Files: 
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
        if "readme2" in d.file:
            print(Fore.WHITE+Style.NORMAL,c.files[3],end=" ")
        if "readme3" in d.file:
            print(Fore.WHITE+Style.NORMAL,c.files[4],end=" ")
        if "amethyst" in d.file:
            print(Fore.MAGENTA+Style.BRIGHT,c.files[10],end=" ")
        if "diamond" in d.file:
            print(Fore.CYAN+Style.BRIGHT,c.files[11],end=" ")
        
        
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
        if d.ruby_chance > 68:
            d.file.append(str(c.files[5]))
            print(Fore.RED+Style.BRIGHT,c.files[5],end=" ")
        if d.amethyst_chance > 47:
            d.file.append(str(c.files[10]))
            print(Fore.MAGENTA+Style.BRIGHT,c.files[10],end=" ")    
        if d.diamond_chance > 57:
            d.file.append(str(c.files[11]))
            print(Fore.CYAN+Style.BRIGHT,c.files[11],end=" ")
        
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
            
            if d.kernelcode_chance >= 37 and d.kernelsolved==False and d.kernelread==False:
                if d.kernelread == False:
                    print(c.specialreadmetexts[0],end=" ")
                    d.kernelcode=random.randint(111111,999999)
                    print(d.kernelcode,end="")
                    d.readme.append(str(c.specialreadmetexts[0])+" "+str(d.kernelcode))
                    d.kernelread=True
                    d.kernelcode_chance = 0
                    
            elif d.codex_chance >= 37 and d.codexsolved==False and d.codexread==False and d.kernelsolved==True and d.chromasolved==True:
                if d.codexread == False:
                    codex = dict(random.sample(list(c.latinnums.items()), 3))
                    print(c.specialreadmetexts[1])
                    print(*codex.keys(), end="")
                    d.readme.append(str(c.specialreadmetexts[1]))
                    d.readme.append("".join(codex.keys()))
                    d.codexnum = list(codex.values())
                    d.codexread=True
                    d.codex_chance = 0
                    
            elif d.chroma_chance >= 35 and d.chromasolved==False and d.chromaread==False and d.kernelsolved==True:
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
                d.kernelcode_chance = random.randint(1,40)
            if d.codexread==False:
                d.codex_chance = random.randint(1,40) 
            if d.chromaread==False:
                d.chroma_chance = random.randint(1,40)
            d.bonus_chance = random.randint(1,20)
            readmescore = random.randint(1,20)
            d.passwd_chance = random.randint(1,40)
            
            if d.kernelcode_chance >= 37 and d.kernelsolved==False and d.kernelread==False:
                if d.kernelread == False:
                    print(c.specialreadmetexts[0],end=" ")
                    d.kernelcode=random.randint(111111,999999)
                    print(d.kernelcode,end="")
                    d.readme2.append(str(c.specialreadmetexts[0])+" "+str(d.kernelcode))
                    d.kernelread=True
                    d.kernelcode_chance = 0
                    
            elif d.codex_chance >= 37 and d.codexsolved==False and d.codexread==False and d.kernelsolved==True and d.chromasolved==True:
                if d.codexread == False:
                    codex = dict(random.sample(list(c.latinnums.items()), 3))
                    print(c.specialreadmetexts[1])
                    print(*codex.keys(), end="")
                    d.readme2.append(str(c.specialreadmetexts[1]))
                    d.readme2.append("".join(codex.keys()))
                    d.codexnum = list(codex.values())
                    d.codexread=True
                    d.codex_chance = 0
            
            elif d.chroma_chance >= 35 and d.chromasolved==False and d.chromaread==False and d.kernelsolved==True:
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
                d.kernelcode_chance = random.randint(1,40)
            if d.codexread==False:
                d.codex_chance = random.randint(1,40) 
            if d.chromaread==False:
                d.chroma_chance = random.randint(1,40)
            d.bonus_chance = random.randint(1,20)
            readmescore = random.randint(1,20)
            d.passwd_chance = random.randint(1,40)
            
            if d.kernelcode_chance >= 37 and d.kernelsolved==False and d.kernelread==False:
                if d.kernelread == False:
                    print(c.specialreadmetexts[0],end=" ")
                    d.kernelcode=random.randint(111111,999999)
                    print(d.kernelcode,end="")
                    d.readme3.append(str(c.specialreadmetexts[0])+" "+str(d.kernelcode))
                    d.kernelread=True
                    d.kernelcode_chance = 0
                    
            elif d.codex_chance >= 37 and d.codexsolved==False and d.codexread==False and d.kernelsolved==True and d.chromasolved==True:
                if d.codexread == False:
                    codex = dict(random.sample(list(c.latinnums.items()), 3))
                    print(c.specialreadmetexts[1])
                    print(*codex.keys(), end="")
                    d.readme3.append(str(c.specialreadmetexts[1]))
                    d.readme3.append("".join(codex.keys()))
                    d.codexnum = list(codex.values())
                    d.codexread=True
                    d.codex_chance = 0
                
            elif d.chroma_chance >= 35 and d.chromasolved==False and d.chromaread==False and d.kernelsolved==True:
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
            
f = Files()