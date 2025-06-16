import time
import random
from colorama import Fore, Style

score = 0
dirs=["bin","boot","dev","etc","lib","mnt","opt","proc","run","srv","sys","tmp","usr","var","dir","tux","linux","localhost","local",
      "bin2","boot2","dev2","etc2","lib2","mnt2","opt2","proc2","run2","srv2","sys2","tmp2","usr2","var2","dir2","tux2","linux2","localhost2","local2",
      "bin3","boot3","dev3","etc3","lib3","mnt3","opt3","proc3","run3","srv3","sys3","tmp3","usr3","var3","dir3","tux3","linux3","localhost3","local3"]
files=["bonus","easteregg","readme","unknown","codex","kernelcode"]
memory=[]
dir=[]
names=[]
names_memory=[]
gendir=[]
genfiles=[]
layer = 1
wentback=False
bonuses = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
for i in range(random.randint(2,7)):
    names.append(str(random.choice(dirs)))
    print(Fore.BLUE+Style.BRIGHT,names[i],end="         ")
for i in names:
    for i in range(random.randint(2,7)):
        gendir.append(str(random.choice(dirs)))
    dir.append(list(gendir))
    gendir.clear()
dirlen=len(dir)
print(Style.RESET_ALL)
print("names - "+str(names))
print("memory - "+str(memory))
print("namesmemory - "+str(names_memory))
print("dir - "+str(dir))
inp = input("player@termadventure ~ ")
syntax = inp.split(" ")
syntax+=["..","cat"]

while True:
    if wentback == False:
        if inp == str(syntax[0])+" "+str(syntax[1]):
            if syntax[1] in names: #cd dest
                layer+=1
                empty_chance = random.randint(1,8)
                print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                if empty_chance < 5:
                    memory.clear()
                    memory+=dir
                    names_memory.clear()
                    names_memory+=names
                    names.clear()
                    dir.clear()
                    empty_chance = random.randint(1,8)
                    bonus_chance = random.randint(1,15)
                    easter_chance = random.randint(1,15)
                    readme_chance = random.randint(1,15)
                    unknown_chance = random.randint(1,15)
                    if syntax[1] == names_memory[0]:
                        for i in range(len(memory[0])):
                            print(Fore.BLUE+Style.BRIGHT,memory[0][i],end="         ")
                            names.append(memory[0][i])
                        for i in memory[0]:
                            for i in range(random.randint(2,7)):
                                gendir.append(str(random.choice(dirs)))
                            dir.append(list(gendir))
                            gendir.clear()
                    elif syntax[1] == names_memory[1]:
                        for i in range(len(memory[1])):
                            print(Fore.BLUE+Style.BRIGHT,memory[1][i],end="         ")
                            names.append(memory[1][i])
                        for i in memory[1]:
                                for i in range(random.randint(2,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                    elif syntax[1] == names_memory[2]:
                        for i in range(len(memory[2])):
                            print(Fore.BLUE+Style.BRIGHT,memory[2][i],end="         ")
                            names.append(memory[2][i])
                        for i in memory[2]:
                                for i in range(random.randint(2,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                    elif syntax[1] == names_memory[3]:
                        for i in range(len(memory[3])):
                            print(Fore.BLUE+Style.BRIGHT,memory[3][i],end="         ")
                            names.append(memory[3][i])
                        for i in memory[3]:
                                for i in range(random.randint(2,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                    elif syntax[1] == names_memory[4]:
                        for i in range(len(memory[4])):
                            print(Fore.BLUE+Style.BRIGHT,memory[4][i],end="         ")
                            names.append(memory[4][i])
                        for i in memory[4]:
                                for i in range(random.randint(2,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                    elif syntax[1] == names_memory[5]:
                        for i in range(len(memory[5])):
                            print(Fore.BLUE+Style.BRIGHT,memory[5][i],end="         ")
                            names.append(memory[5][i])
                        for i in memory[5]:
                                for i in range(random.randint(2,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                    elif syntax[1] == names_memory[6]:
                        for i in range(len(memory[6])):
                            print(Fore.BLUE+Style.BRIGHT,memory[6][i],end="         ")
                            names.append(memory[6][i])
                        for i in memory[6]:
                                for i in range(random.randint(2,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                    dirlen=len(dir)
                    if bonus_chance > 12:
                        genfiles.append(str(files[0]))
                        print(Fore.GREEN+Style.BRIGHT,files[0],end="         ")
                    if easter_chance > 14:
                        genfiles.append(str(files[1]))
                        print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                    if readme_chance > 12:
                        genfiles.append(str(files[2]))
                        print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                    if unknown_chance > 12:
                        genfiles.append(str(files[3]))
                        print(Fore.RED+Style.BRIGHT,files[3],end="         ")
                    print(Style.RESET_ALL)
                    lastdir=syntax[1]
                    print("names - "+str(names))
                    print("memory - "+str(memory))
                    print("namesmemory - "+str(names_memory))
                    print("dir - "+str(dir))
                    inp = input("player@termadventure ~ ")
                    syntax = inp.split(" ")
                    syntax+=["..","cat"]
                elif empty_chance >= 5: #generate dirs
                    # bonus_chance = random.randint(1,15)
                    # easter_chance = random.randint(1,15)
                    # readme_chance = random.randint(1,15)
                    # unknown_chance = random.randint(1,15)
                    # for i in range(random.randint(2,7)):
                    #     names.append(str(random.choice(dirs)))
                    # for i in names:
                    #     for i in range(random.randint(2,7)):
                    #         gendir.append(str(random.choice(dirs)))
                    #     dir.append(list(gendir))
                    #     gendir.clear()
                    #     genfiles.clear()
                    # dirlen=len(dir)
                    # if bonus_chance > 8:
                    #     genfiles.append(str(files[0]))
                    # if easter_chance > 14:
                    #     genfiles.append(str(files[1]))
                    # if readme_chance > 8:
                    #     genfiles.append(str(files[2]))
                    # if unknown_chance > 10:
                    #     genfiles.append(str(files[3]))
                    print(Fore.YELLOW,"*"+Fore.WHITE,"Directory is empty",end="         ")
                    print(Style.RESET_ALL)
                    print("names - "+str(names))
                    print("memory - "+str(memory))
                    print("namesmemory - "+str(names_memory))
                    print("dir - "+str(dir))
                    inp = input("player@termadventure ~ ")
                    syntax = inp.split(" ")
                    syntax+=["..","cat"]
            elif inp == str(syntax[0])+" "+str(syntax[2]): #cd ..
                layer-=1
                print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                for i in range(len(names)):
                    print(Fore.BLUE+Style.BRIGHT,names[i], end="         ")
                if "bonus" in genfiles:
                    print(Fore.GREEN+Style.BRIGHT,files[0],end="         ")
                if "easteregg" in genfiles:
                    print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                if "readme" in genfiles:
                    print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                if "unknown" in genfiles:
                    print(Fore.RED+Style.BRIGHT,files[3],end="         ")
                print(Style.RESET_ALL)
                print("names - "+str(names))
                print("memory - "+str(memory))
                print("namesmemory - "+str(names_memory))
                print("dir - "+str(dir))
                wentback=True
                inp = input("player@termadventure ~ ")
                syntax.clear()
                syntax = inp.split(" ")
                syntax+=["..","cat"]
        elif inp == files[0]:
            if inp == "bonus" and syntax[0] in names: #bonus
                bonusscore = random.choice(bonuses)
                if bonusscore == 1000:
                    print(Fore.GREEN,"* Bonus! +1000pts",end="         ")
                    score+=1000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 2000:
                    print(Fore.GREEN,"* Bonus! +2000pts",end="         ")
                    score+=2000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 3000:
                    print(Fore.GREEN,"* Bonus! +3000pts",end="         ")
                    score+=3000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 4000:
                    print(Fore.GREEN,"* Bonus! +4000pts",end="         ")
                    score+=4000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 5000:
                    print(Fore.GREEN,"* Bonus! +5000pts",end="         ")
                    score+=5000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 6000:
                    print(Fore.GREEN,"* Bonus! +6000pts",end="         ")
                    score+=6000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 7000:
                    print(Fore.GREEN,"* Bonus! +7000pts",end="         ")
                    score+=7000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 8000:
                    print(Fore.GREEN,"* Bonus! +8000pts",end="         ")
                    score+=8000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 9000:
                    print(Fore.GREEN,"* Bonus! +9000pts",end="         ")
                    score+=9000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 10000:
                    print(Fore.YELLOW,"* Bonus! +10000pts",end="         ")
                    score+=10000
                    names.remove("bonus")
                    print(Style.RESET_ALL)
                inp = input("player@termadventure ~ ")
                syntax.clear()
                syntax = inp.split(" ")
                syntax+=["..","cat"]
        elif inp == files[1]:
            if inp == "easteregg" and syntax[0] in names: #easteregg
                print(Fore.YELLOW,"* Easter egg found! +10000pts",end="         ")
                score+=10000
                names.remove("easteregg")
                print(Style.RESET_ALL)
                inp = input("player@termadventure ~ ")
                syntax.clear()
                syntax = inp.split(" ")
                syntax+=["..","cat"]
    if wentback == True:
        if inp == str(syntax[0])+" "+str(syntax[1]):  
            if syntax[0] == "cd" and syntax[1] in names: #cd (newdest)
                if syntax[1] in names: #cd dest
                    layer+=1
                    empty_chance = random.randint(1,8)
                    print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                    if empty_chance < 5:
                        wentback = False
                        memory.clear()
                        memory+=dir
                        names_memory.clear()
                        names_memory+=names
                        names.clear()
                        dir.clear()
                        empty_chance = random.randint(1,8)
                        bonus_chance = random.randint(1,15)
                        easter_chance = random.randint(1,15)
                        readme_chance = random.randint(1,15)
                        unknown_chance = random.randint(1,15)
                        if syntax[1] == names_memory[0]:
                            for i in range(len(memory[0])):
                                print(Fore.BLUE+Style.BRIGHT,memory[0][i],end="         ")
                                names.append(memory[0][i])
                            for i in memory[0]:
                                for i in range(random.randint(2,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                        elif syntax[1] == names_memory[1]:
                            for i in range(len(memory[1])):
                                print(Fore.BLUE+Style.BRIGHT,memory[1][i],end="         ")
                                names.append(memory[1][i])
                            for i in memory[1]:
                                    for i in range(random.randint(2,7)):
                                        gendir.append(str(random.choice(dirs)))
                                    dir.append(list(gendir))
                                    gendir.clear()
                        elif syntax[1] == names_memory[2]:
                            for i in range(len(memory[2])):
                                print(Fore.BLUE+Style.BRIGHT,memory[2][i],end="         ")
                                names.append(memory[2][i])
                            for i in memory[2]:
                                    for i in range(random.randint(2,7)):
                                        gendir.append(str(random.choice(dirs)))
                                    dir.append(list(gendir))
                                    gendir.clear()
                        elif syntax[1] == names_memory[3]:
                            for i in range(len(memory[3])):
                                print(Fore.BLUE+Style.BRIGHT,memory[3][i],end="         ")
                                names.append(memory[3][i])
                            for i in memory[3]:
                                    for i in range(random.randint(2,7)):
                                        gendir.append(str(random.choice(dirs)))
                                    dir.append(list(gendir))
                                    gendir.clear()
                        elif syntax[1] == names_memory[4]:
                            for i in range(len(memory[4])):
                                print(Fore.BLUE+Style.BRIGHT,memory[4][i],end="         ")
                                names.append(memory[4][i])
                            for i in memory[4]:
                                    for i in range(random.randint(2,7)):
                                        gendir.append(str(random.choice(dirs)))
                                    dir.append(list(gendir))
                                    gendir.clear()
                        elif syntax[1] == names_memory[5]:
                            for i in range(len(memory[5])):
                                print(Fore.BLUE+Style.BRIGHT,memory[5][i],end="         ")
                                names.append(memory[5][i])
                            for i in memory[5]:
                                    for i in range(random.randint(2,7)):
                                        gendir.append(str(random.choice(dirs)))
                                    dir.append(list(gendir))
                                    gendir.clear()
                        elif syntax[1] == names_memory[6]:
                            for i in range(len(memory[6])):
                                print(Fore.BLUE+Style.BRIGHT,memory[6][i],end="         ")
                                names.append(memory[6][i])
                            for i in memory[6]:
                                    for i in range(random.randint(2,7)):
                                        gendir.append(str(random.choice(dirs)))
                                    dir.append(list(gendir))
                                    gendir.clear()
                        dirlen=len(dir)
                        if bonus_chance > 12:
                            genfiles.append(str(files[0]))
                            print(Fore.GREEN+Style.BRIGHT,files[0],end="         ")
                        if easter_chance > 14:
                            genfiles.append(str(files[1]))
                            print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                        if readme_chance > 12:
                            genfiles.append(str(files[2]))
                            print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                        if unknown_chance > 12:
                            genfiles.append(str(files[3]))
                            print(Fore.RED+Style.BRIGHT,files[3],end="         ")
                print(Style.RESET_ALL)
                lastdir=syntax[1]
                print("names - "+str(names))
                print("memory - "+str(memory))
                print("namesmemory - "+str(names_memory))
                print("dir - "+str(dir))
                inp = input("player@termadventure ~ ")
                syntax.clear()
                syntax = inp.split(" ")
                syntax+=["..","cat"]
            if inp == "cd .." and wentback == True:
                print(Fore.YELLOW,"*"+Fore.WHITE,"You can't go back now!",end="         ")
                print(Style.RESET_ALL)
                inp = input("player@termadventure ~ ")
                syntax = inp.split(" ")
                syntax+=["..","cat"] 
        if syntax[0] == "bonus" and syntax[0] in names_memory: #bonus
                bonusscore = random.choice(bonuses)
                if bonusscore == 1000:
                    print(Fore.GREEN,"* Bonus! +1000pts",end="         ")
                    score+=1000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 2000:
                    print(Fore.GREEN,"* Bonus! +2000pts",end="         ")
                    score+=2000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 3000:
                    print(Fore.GREEN,"* Bonus! +3000pts",end="         ")
                    score+=3000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 4000:
                    print(Fore.GREEN,"* Bonus! +4000pts",end="         ")
                    score+=4000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 5000:
                    print(Fore.GREEN,"* Bonus! +5000pts",end="         ")
                    score+=5000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 6000:
                    print(Fore.GREEN,"* Bonus! +6000pts",end="         ")
                    score+=6000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 7000:
                    print(Fore.GREEN,"* Bonus! +7000pts",end="         ")
                    score+=7000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 8000:
                    print(Fore.GREEN,"* Bonus! +8000pts",end="         ")
                    score+=8000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 9000:
                    print(Fore.GREEN,"* Bonus! +9000pts",end="         ")
                    score+=9000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                elif bonusscore == 10000:
                    print(Fore.YELLOW,"* Bonus! +10000pts",end="         ")
                    score+=10000
                    names_memory.remove("bonus")
                    print(Style.RESET_ALL)
                inp = input("player@termadventure ~ ")
                syntax.clear()
                syntax = inp.split(" ")
                syntax+=["..","cat"]
        if syntax[0] == "easteregg" and syntax[0] in names_memory: #easteregg
            print(Fore.YELLOW,"* Easter egg found! +10000pts",end="         ")
            score+=10000
            names_memory.remove("easteregg")
            print(Style.RESET_ALL)
            inp = input("player@termadventure ~ ")
            syntax.clear()
            syntax = inp.split(" ")
            syntax+=["..","cat"]
        
    if layer == 50:
        break