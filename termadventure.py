import time
import random
import os
from colorama import Fore, Style

score = 0
dirs=["bin","boot","dev","etc","lib","mnt","opt","proc","run","srv","sys","tmp","usr","var","dir","tux","linux","localhost","local","doc","share","tmpfs","home","udev","tty1","sda1","sdb1","sdc1","nvme0n1p1",
      "bin2","boot2","dev2","etc2","lib2","mnt2","opt2","proc2","run2","srv2","sys2","tmp2","usr2","var2","dir2","tux2","linux2","localhost2","local2","doc2","share2","tmpfs2","home2","udev2","tty2","sda2","sdb2","sdc2","nvme0n1p2",
      "bin3","boot3","dev3","etc3","lib3","mnt3","opt3","proc3","run3","srv3","sys3","tmp3","usr3","var3","dir3","tux3","linux3","localhost3","local3","doc3","share3","tmpfs3","home3","udev3","tty3","sda3","sdb3","sdc3","nvme0n1p3"]   
files=["bonus","easteregg","readme","unknown","codex","kernelcode","hex"]
memory=[]
dir=[]
names=[]
names_memory=[]
gendir=[]
file=[]
file_memory=[]
layer = 1
wentbackempty=False
wentback=False
inemptydir=False
bonuses = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))

for i in range(random.randint(4,8)):
    names.append(str(random.choice(dirs)))
    print(Fore.BLUE+Style.BRIGHT,names[i],end="         ")
    
for i in names:
    for i in range(random.randint(4,8)):
        gendir.append(str(random.choice(dirs)))
    dir.append(list(gendir))
    gendir.clear()
    
dirlen=len(dir)

while True:
    
    if wentbackempty == False:
        print(Style.RESET_ALL)
        inp = input("player@termadventure ~ ")
        syntax = inp.split(" ")
        syntax+=["..","cat"]
        
        if inp == str(syntax[0])+" "+str(syntax[1]):
            if syntax[1] in names: #cd dest
                layer+=1
                empty_chance = random.randint(1,8)
                print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                
                if empty_chance < 7:
                    memory.clear()
                    memory+=dir
                    names_memory.clear()
                    names_memory+=names
                    names.clear()
                    dir.clear()
                    file_memory.clear()
                    file_memory+=file
                    file.clear()
                    bonus_chance = random.randint(1,15)
                    easter_chance = random.randint(1,15)
                    readme_chance = random.randint(1,15)
                    unknown_chance = random.randint(1,15)
                    
                    if syntax[1] == names_memory[0]:
                        for i in range(len(memory[0])):
                            print(Fore.BLUE+Style.BRIGHT,memory[0][i],end="         ")
                            names.append(memory[0][i])
                        for i in memory[0]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[1]:
                        for i in range(len(memory[1])):
                            print(Fore.BLUE+Style.BRIGHT,memory[1][i],end="         ")
                            names.append(memory[1][i])
                        for i in memory[1]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[2]:
                        for i in range(len(memory[2])):
                            print(Fore.BLUE+Style.BRIGHT,memory[2][i],end="         ")
                            names.append(memory[2][i])
                        for i in memory[2]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[3]:
                        for i in range(len(memory[3])):
                            print(Fore.BLUE+Style.BRIGHT,memory[3][i],end="         ")
                            names.append(memory[3][i])
                        for i in memory[3]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[4]:
                        for i in range(len(memory[4])):
                            print(Fore.BLUE+Style.BRIGHT,memory[4][i],end="         ")
                            names.append(memory[4][i])
                        for i in memory[4]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[5]:
                        for i in range(len(memory[5])):
                            print(Fore.BLUE+Style.BRIGHT,memory[5][i],end="         ")
                            names.append(memory[5][i])
                        for i in memory[5]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[6]:
                        for i in range(len(memory[6])):
                            print(Fore.BLUE+Style.BRIGHT,memory[6][i],end="         ")
                            names.append(memory[6][i])
                        for i in memory[6]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    dirlen=len(dir)
                    
                    if bonus_chance > 12:
                        file.append(str(files[0]))
                        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
                    if easter_chance > 14:
                        file.append(str(files[1]))
                        print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")                      
                    if readme_chance > 12:
                        file.append(str(files[2]))
                        print(Fore.WHITE+Style.NORMAL,files[2],end="         ")        
                    if unknown_chance > 12:
                        file.append(str(files[3]))
                        print(Fore.RED+Style.BRIGHT,files[3],end="         ")
                        
                elif empty_chance >= 7:
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
                        
                    inemptydir=True
                    print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                    
            elif inp == str(syntax[0])+" "+str(syntax[2]) and inemptydir == True: #cd .. when entered empty
                layer-=1
                print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                
                for i in range(len(names)):
                    print(Fore.BLUE+Style.BRIGHT,names[i], end="         ")
                if "bonus" in file:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
                if "easteregg" in file:
                    print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                if "readme" in file:
                    print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                if "unknown" in file:
                    print(Fore.RED+Style.BRIGHT,files[3],end="         ")
                    
                wentbackempty=True
                inemptydir=False
                
            elif inp == str(syntax[0])+" "+str(syntax[2]) and inemptydir == False: #cd ..
                layer-=1
                print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                
                for i in range(len(names_memory)):
                    print(Fore.BLUE+Style.BRIGHT,names_memory[i], end="         ")
                if "bonus" in file_memory:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
                if "easteregg" in file_memory:
                    print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                if "readme" in file_memory:
                    print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                if "unknown" in file_memory:
                    print(Fore.RED+Style.BRIGHT,files[3],end="         ")
                    
                wentback=True
                
        elif inp == files[0]:
            if inp == "bonus" and syntax[0] in file: #bonus
                bonusscore = random.choice(bonuses)
                
                if bonusscore == 1000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +1000pts",end="         ")
                    score+=1000
                    file.remove("bonus")
                elif bonusscore == 2000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +2000pts",end="         ")
                    score+=2000
                    file.remove("bonus")
                elif bonusscore == 3000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +3000pts",end="         ")
                    score+=3000
                    file.remove("bonus")
                elif bonusscore == 4000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +4000pts",end="         ")
                    score+=4000
                    file.remove("bonus")
                elif bonusscore == 5000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +5000pts",end="         ")
                    score+=5000
                    file.remove("bonus")
                elif bonusscore == 6000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +6000pts",end="         ")
                    score+=6000
                    file.remove("bonus")
                elif bonusscore == 7000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +7000pts",end="         ")
                    score+=7000
                    file.remove("bonus")
                elif bonusscore == 8000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +8000pts",end="         ")
                    score+=8000
                    file.remove("bonus")
                elif bonusscore == 9000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +9000pts",end="         ")
                    score+=9000
                    file.remove("bonus")
                elif bonusscore == 10000:
                    print(Fore.YELLOW+Style.BRIGHT,"* Bonus! +10000pts",end="         ")
                    score+=10000
                    file.remove("bonus")
                    
        elif inp == files[1]:
            if inp == "easteregg" and syntax[0] in file: #easteregg
                print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10000pts",end="         ")
                score+=10000
                file.remove("easteregg")
                
        elif inp == files[3]:
            if inp == "unknown" and syntax[0] in file:
                print("\nplayer@termadventure ~ ", end="")
                time.sleep(0.2)
                print("sudo rm -rf --no-preserve-root")
                time.sleep(0.4)
                os.system("cls")
                time.sleep(1)
                print(Fore.RED+Style.BRIGHT,"* "+Fore.WHITE+Style.NORMAL+"Game over!")
                inp == input()
                
    if wentback == True:
        
        print(Style.RESET_ALL)
        inp = input("player@termadventure ~ ")
        syntax = inp.split(" ")
        syntax+=["..","cat"]
        
        if inp == str(syntax[0])+" "+str(syntax[1]):
            if syntax[0] == "cd" and syntax[1] in names_memory:
                
                if empty_chance < 7:
                    layer+=1
                    names.clear()
                    dir.clear()
                    bonus_chance = random.randint(1,15)
                    easter_chance = random.randint(1,15)
                    readme_chance = random.randint(1,15)
                    unknown_chance = random.randint(1,15)
                    print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                    
                    if syntax[1] == names_memory[0]:
                        for i in range(len(memory[0])):
                            print(Fore.BLUE+Style.BRIGHT,memory[0][i],end="         ")
                            names.append(memory[0][i])
                        for i in memory[0]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[1]:
                        for i in range(len(memory[1])):
                            print(Fore.BLUE+Style.BRIGHT,memory[1][i],end="         ")
                            names.append(memory[1][i])
                        for i in memory[1]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[2]:
                        for i in range(len(memory[2])):
                            print(Fore.BLUE+Style.BRIGHT,memory[2][i],end="         ")
                            names.append(memory[2][i])
                        for i in memory[2]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[3]:
                        for i in range(len(memory[3])):
                            print(Fore.BLUE+Style.BRIGHT,memory[3][i],end="         ")
                            names.append(memory[3][i])
                        for i in memory[3]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[4]:
                        for i in range(len(memory[4])):
                            print(Fore.BLUE+Style.BRIGHT,memory[4][i],end="         ")
                            names.append(memory[4][i])
                        for i in memory[4]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[5]:
                        for i in range(len(memory[5])):
                            print(Fore.BLUE+Style.BRIGHT,memory[5][i],end="         ")
                            names.append(memory[5][i])
                        for i in memory[5]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    elif syntax[1] == names_memory[6]:
                        for i in range(len(memory[6])):
                            print(Fore.BLUE+Style.BRIGHT,memory[6][i],end="         ")
                            names.append(memory[6][i])
                        for i in memory[6]:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                    dirlen=len(dir)
                    wentback=False
                    
                    if bonus_chance > 12:
                            file.append(str(files[0]))
                            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
                    if easter_chance > 14:
                        file.append(str(files[1]))
                        print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                    if readme_chance > 12:
                        file.append(str(files[2]))
                        print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                    if unknown_chance > 12:
                        file.append(str(files[3]))
                        print(Fore.RED+Style.BRIGHT,files[3],end="         ")
                        
                elif empty_chance >= 7:
                    if syntax[1] == names_memory[0]:
                        dir[0].append("empty")
                    elif syntax[1] == names_memory[1]:
                        dir[1].append("empty")
                    elif syntax[1] == names_memory[2]:
                        dir[2].append("empty")
                    elif syntax[1] == names_memory[3]:
                        dir[3].append("empty")
                    elif syntax[1] == names_memory[4]:
                        dir[4].append("empty")
                    elif syntax[1] == names_memory[5]:
                        dir[5].append("empty")
                    elif syntax[1] == names_memory[6]:
                        dir[6].append("empty")
                        
                    inemptydir=True
                    print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                    
    if wentbackempty == True:
        print(Style.RESET_ALL)
        inp = input("player@termadventure ~ ")
        syntax = inp.split(" ")
        syntax+=["..","cat"]
        
        if inp == str(syntax[0])+" "+str(syntax[1]):  
            if syntax[0] == "cd" and syntax[1] in names: #cd (newdest)
                
                if syntax[1] in names: #cd dest
                    layer+=1
                    empty_chance = random.randint(1,8)
                    bonus_chance = random.randint(1,15)
                    easter_chance = random.randint(1,15)
                    readme_chance = random.randint(1,15)
                    unknown_chance = random.randint(1,15)
                    empty_chance = random.randint(1,8)
                    print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                    
                    if empty_chance < 7:
                        names_memory.clear()
                        names_memory+=names
                        names.clear()
                        memory.clear()
                        memory+=dir
                        dir.clear()
                        file_memory.clear()
                        file_memory+=file
                        file.clear()
                        
                        if syntax[1] == names_memory[0]: #if name[x] print dir[x]
                            if "empty" not in memory[0]:
                                for i in range(len(memory[0])):
                                    print(Fore.BLUE+Style.BRIGHT,memory[0][i], end="         ")
                                    names.append(memory[0][i])
                            else:
                                print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                        elif syntax[1] == names_memory[1]:
                            if "empty" not in memory[1]:
                                for i in range(len(memory[1])):
                                    print(Fore.BLUE+Style.BRIGHT,memory[1][i], end="         ")
                                    names.append(memory[1][i])
                            else:
                                print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                        elif syntax[1] == names_memory[2]:
                            if "empty" not in memory[2]:
                                for i in range(len(memory[2])):
                                    print(Fore.BLUE+Style.BRIGHT,memory[2][i], end="         ")
                                    names.append(memory[2][i])
                            else:
                                print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                        elif syntax[1] == names_memory[3]:
                            if "empty" not in memory[3]:
                                for i in range(len(memory[3])):
                                    print(Fore.BLUE+Style.BRIGHT,memory[3][i], end="         ")
                                    names.append(memory[3][i])
                            else:
                                print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                        elif syntax[1] == names_memory[4]:
                            if "empty" not in memory[4]:
                                for i in range(len(memory[4])):
                                    print(Fore.BLUE+Style.BRIGHT,memory[4][i], end="         ")
                                    names.append(memory[4][i])
                            else:
                                print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                        elif syntax[1] == names_memory[5]:
                            if "empty" not in memory[5]:
                                for i in range(len(memory[5])):
                                    print(Fore.BLUE+Style.BRIGHT,memory[5][i], end="         ")
                                    names.append(memory[5][i])
                            else:
                                print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                        elif syntax[1] == names_memory[6]:
                            if "empty" not in memory[6]:
                                for i in range(len(memory[6])):
                                    print(Fore.BLUE+Style.BRIGHT,memory[6][i], end="         ")
                                    names.append(memory[6][i])
                            else:
                                print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                        for i in names:
                            for i in range(random.randint(4,8)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                            
                        dirlen=len(dir)
                        
                        if bonus_chance > 12:
                            file.append(str(files[0]))
                            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
                        if easter_chance > 14:
                            file.append(str(files[1]))
                            print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                        if readme_chance > 12:
                            file.append(str(files[2]))
                            print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                        if unknown_chance > 12:
                            file.append(str(files[3]))
                            print(Fore.RED+Style.BRIGHT,files[3],end="         ")
                            
                    elif empty_chance >= 7:
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
                        inemptydir=True
                        print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                        
                    wentbackempty=False
                    
            if inp == "cd .." and wentbackempty == True:
                print(Fore.YELLOW,"*"+Fore.WHITE,"You can't go back now!",end="         ")
                
        elif inp == "bonus" and syntax[0] in file: #bonus
                bonusscore = random.choice(bonuses)
                if bonusscore == 1000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +1000pts",end="         ")
                    score+=1000
                    file.remove("bonus")
                elif bonusscore == 2000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +2000pts",end="         ")
                    score+=2000
                    file.remove("bonus")
                elif bonusscore == 3000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +3000pts",end="         ")
                    score+=3000
                    file.remove("bonus")
                elif bonusscore == 4000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +4000pts",end="         ")
                    score+=4000
                    file.remove("bonus")
                elif bonusscore == 5000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +5000pts",end="         ")
                    score+=5000
                    file.remove("bonus")
                elif bonusscore == 6000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +6000pts",end="         ")
                    score+=6000
                    file.remove("bonus")
                elif bonusscore == 7000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +7000pts",end="         ")
                    score+=7000
                    file.remove("bonus")
                elif bonusscore == 8000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +8000pts",end="         ")
                    score+=8000
                    file.remove("bonus")
                elif bonusscore == 9000:
                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,"* Bonus! +9000pts",end="         ")
                    score+=9000
                    file.remove("bonus")
                elif bonusscore == 10000:
                    print(Fore.YELLOW+Style.BRIGHT,"* Bonus! +10000pts",end="         ")
                    score+=10000
                    file.remove("bonus")
                    
        elif syntax[0] == "easteregg" and syntax[0] in file: #easteregg
            print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10000pts",end="         ")
            score+=10000
            file.remove("easteregg")
        
    if layer == 49:
        break