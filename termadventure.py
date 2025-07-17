import time
import random
import os
import sys
from colorama import Fore, Style

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
dirs=["bin","boot","dev","etc","lib","mnt","opt","proc","run","srv","sys","tmp","usr","var","dir","tux","linux","localhost","local","doc","share","tmpfs","home","udev","tty1","sbin","src",
      "lost+found","include","man","log","cache","lock","spool","sda1","sdb1","sdc1",
      "bin2","boot2","dev2","etc2","lib2","mnt2","opt2","proc","run2","srv2","sys2","tmp2","usr2","var2","dir2","tux2","linux2","localhost2","local2","doc2","share2","tmpfs2","home2","udev2",
      "tty2","sbin2","src2","lost+found2","include2","man2","log2","cache2","lock2","spool2","sda2","sdb2","sdc2",
      "bin3","boot3","dev3","etc3","lib3","mnt3","opt3","proc3","run3","srv3","sys3","tmp3","usr3","var3","dir3","tux3","linux3","localhost3","local3","doc3","share3","tmpfs3",
      "home3","udev3","tty3","sbin3","src3","lost+found3","include3","man3","log3","cache3","lock3","spool3","sda3","sdb3","sdc3",
      "bin4","boot4","dev4","etc4","lib4","mnt4","opt4","proc4","run4","srv4","sys4","tmp4","usr4","var4","dir4","tux4","linux4","localhost4","local4","doc4","share4",
      "tmpfs4","home4","udev4","tty4","sbin4","src4","lost+found4","include4","man4","log4","cache4","lock4","spool4","sda4","sdb4","sdc4"]   
files=["bonus","easteregg","readme","readme2","readme3","unknown","codex","kernelcode"]
specialreadmetexts=["Linux termadventure 6.15.5-zen1-1-zen x86_64 GNU/Linux",
"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
""","here are some points for you: ","your score is currently "]
readmetexts=["hello world","nothing to find here","thank you player, but the thing you're looking for is in another readme file!",
"penguin is watching","nothing","if it works, don't touch it","it's free real estate","open source for the win","what's up","""
To do list:
- buy amd gpu
- get rid of windows
- install arch linux on first drive
- install gentoo on second drive
""","i am king terry the terrible",";-)","herzlich wilkommen","no looking back"]
rootpasswords=["********","123","root","admin","password","administrator","linuxthebest"]
bonuses = [1000,2000,3000,4000,5000]

print(Fore.GREEN+Style.BRIGHT,r"""
  ______                    ___       __                 __                
 /_  __/__  _________ ___  /   | ____/ /   _____  ____  / /___  __________ 
  / / / _ \/ ___/ __ `__ \/ /| |/ __  / | / / _ \/ __ \/ __/ / / / ___/ _ \
 / / /  __/ /  / / / / / / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/
/_/  \___/_/  /_/ /_/ /_/_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/ 
""", end="")
print(Fore.WHITE,"Written in Python by Atomix, 8.07.2025                        Version 0.2")
print(Style.RESET_ALL)
print(Fore.GREEN,"* "+Fore.WHITE+Style.BRIGHT+"play"+Style.NORMAL,"- start the game")
print(Fore.GREEN,"* "+Fore.WHITE+Style.BRIGHT+"info"+Style.NORMAL,"- show description")
print(Fore.GREEN,"* "+Fore.WHITE+Style.BRIGHT+"quit"+Style.NORMAL,"- leave the game")

while True:
    inp = input(Style.RESET_ALL+"\nplayer@termadventure $ ")

    if inp == "info" or inp == "i":
        print("""
* Explore the seemingly infinite Linux kernel containing directories and files.
* You may find a lot of interesting things, which can give you points.
* But unknown files may delete your system (not literally), so be careful!
* There are also readme files, which can contain codes for specific programs.
* Reach layer 50 to get to the root directory. 
* For the full guidebook, check out the README file in the repository.
            """)
    if inp == "quit" or inp == "q":
        exit()
    if inp == "play" or inp == "p":
        break
    
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
    layer = 1
    codexprg_chance=0
    kernelcodeprg_chance=0
    wentbackempty=False
    inemptydir=False
    kernelread=False
    codexread=False
    kernelsolved=False
    codexsolved=False
    print("\n")
    print("Generating directories")
    for i in range (101):
        print("\r"+str(int(i/2))+"/50"+" "+i*"=",end=">",flush=True)
        time.sleep(0.003)
    print("\n")
    print(Fore.GREEN+Style.NORMAL,"*"+Fore.WHITE,"Loading directories ...                                                                           "+Fore.BLUE+Style.BRIGHT,"["+Fore.GREEN,"ok"+Fore.BLUE,"]")
    time.sleep(0.3)
    print(Fore.GREEN+Style.NORMAL,"*"+Fore.WHITE,"Loading bonuses ...                                                                               "+Fore.BLUE+Style.BRIGHT,"["+Fore.GREEN,"ok"+Fore.BLUE,"]")
    time.sleep(0.05)
    print(Fore.GREEN+Style.NORMAL,"*"+Fore.WHITE,"Loading eastereggs ...                                                                            "+Fore.BLUE+Style.BRIGHT,"["+Fore.GREEN,"ok"+Fore.BLUE,"]")
    time.sleep(0.1)
    print(Fore.GREEN+Style.NORMAL,"*"+Fore.WHITE,"Loading unknown files ...                                                                         "+Fore.BLUE+Style.BRIGHT,"["+Fore.GREEN,"ok"+Fore.BLUE,"]")
    time.sleep(0.2)
    print(Fore.GREEN+Style.NORMAL,"*"+Fore.WHITE,"Loading readme files ...                                                                          "+Fore.BLUE+Style.BRIGHT,"["+Fore.GREEN,"ok"+Fore.BLUE,"]")
    time.sleep(0.5)
    print("\n"+Fore.GREEN+Style.NORMAL,"*"+Fore.WHITE,"Let's go!")
    time.sleep(2)
    print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
    
    print(Fore.BLUE+Style.BRIGHT,"home",end="         ")
    while True:
        print(Style.RESET_ALL)
        inp = input("player@termadventure $ ")
        if inp == "cd home":
            break
        elif inp == "help":
            print("""
ls - list directories
cd (dir) - change directory
cd .. - leave the directory
cat (text file) - read the content of the text file
(executable) - run the program or claim bonus
su root - switch to the root user""")
        
    layer+=1
    score+=100
    print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer),end="  ")
    print(Fore.GREEN,"+100 pts")
    for i in range(random.randint(4,7)):
        names.append(str(random.choice(dirs)))
        print(Fore.BLUE+Style.BRIGHT,names[i],end="         ")
        
    for i in names:
        for i in range(random.randint(4,7)):
            gendir.append(str(random.choice(dirs)))
        dir.append(list(gendir))
        gendir.clear()

    while layer < 50:
        
        if kernelsolved == True and codexsolved == True:
            if "readme" in file:
                file.remove("readme")
            if "readme2" in file:
                file.remove("readme2")
            if "readme3" in file:
                file.remove("readme3")

        if inp == "cd .." and inemptydir == False and wentbackempty == False:
            print(Fore.YELLOW,"*"+Fore.WHITE,"Sorry, you can't go back",end="         ")
            
        if inp == "quit" or inp == "q":
            quit()
        
        if inp == "su root":
            time.sleep(0.1)
            prompt = input("Password: ")
            print("su: Authentication failure",end="")
            
        if inp == "help":
            print("""
ls - list directories
cd (dir) - change directory
cd .. - leave the directory
cat (text file) - read the content of the text file
(executable) - run the program or claim bonus
su root - switch to the root user""")
            
        if inp == "ls":
            for i in range(len(names)):
                  print(Fore.BLUE+Style.BRIGHT,names[i],end="         ")
            if "bonus" in file:
                print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
            if "codex" in file:
                print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[5],end="         ")
            if "kernelcode" in file:
                print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[6],end="         ")
            if "easteregg" in file:
                print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
            if "unknown" in file:
                print(Fore.RED+Style.BRIGHT,files[5],end="         ")
            if "readme" in file:
                print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
            if "readme2" in file:
                print(Fore.WHITE+Style.NORMAL,files[3],end="         ")
            if "readme3" in file:
                print(Fore.WHITE+Style.NORMAL,files[4],end="         ")
                
        if inemptydir == True:
            print(Style.RESET_ALL)
            inp = input("player@termadventure $ ")
            syntax = inp.split(" ")
            syntax+=[".."]
            
            if inp == str(syntax[0])+" "+str(syntax[2]) and inemptydir == True and wentbackempty == False: #cd .. when entered empty
                    layer-=1
                    print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
                    
                    for i in range(len(names)):
                        print(Fore.BLUE+Style.BRIGHT,names[i], end="         ")
                    if "bonus" in file:
                        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
                    if "codex" in file:
                        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[6],end="         ")
                    if "kernelcode" in file:
                        print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[7],end="         ")
                    if "easteregg" in file:
                        print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                    if "unknown" in file:
                        print(Fore.RED+Style.BRIGHT,files[5],end="         ")
                    if "readme" in file:
                        print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                    if "readme2" in file:
                        print(Fore.WHITE+Style.NORMAL,files[3],end="         ")
                    if "readme3" in file:
                        print(Fore.WHITE+Style.NORMAL,files[4],end="         ")
                        
                    wentbackempty=True
                    inemptydir=False

        if wentbackempty == False and inemptydir == False:
            print(Style.RESET_ALL)
            inp = input("player@termadventure $ ")
            syntax = inp.split(" ")
            syntax+=[".."]
            
            if inp == str(syntax[0])+" "+str(syntax[1]):
                if syntax[1] in names: #cd dest
                    layer+=1
                    if layer == 50:
                        break
                    empty_chance = random.randint(1,8)
                    print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer),end="  ")
                    
                    if empty_chance < 7:
                        
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
                        if codexread==True:
                            codexprg_chance = random.randint(1,20)
                        if kernelread==True:
                            kernelcodeprg_chance = random.randint(1,20)
                            
                        if syntax[1] == names_memory[0]:
                            for i in range(len(memory[0])):
                                print(Fore.BLUE+Style.BRIGHT,memory[0][i],end="         ")
                                names.append(memory[0][i])
                            for i in memory[0]:
                                for i in range(random.randint(4,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                                
                        elif syntax[1] == names_memory[1]:
                            for i in range(len(memory[1])):
                                print(Fore.BLUE+Style.BRIGHT,memory[1][i],end="         ")
                                names.append(memory[1][i])
                            for i in memory[1]:
                                for i in range(random.randint(4,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                                
                        elif syntax[1] == names_memory[2]:
                            for i in range(len(memory[2])):
                                print(Fore.BLUE+Style.BRIGHT,memory[2][i],end="         ")
                                names.append(memory[2][i])
                            for i in memory[2]:
                                for i in range(random.randint(4,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                                
                        elif syntax[1] == names_memory[3]:
                            for i in range(len(memory[3])):
                                print(Fore.BLUE+Style.BRIGHT,memory[3][i],end="         ")
                                names.append(memory[3][i])
                            for i in memory[3]:
                                for i in range(random.randint(4,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                                
                        elif syntax[1] == names_memory[4]:
                            for i in range(len(memory[4])):
                                print(Fore.BLUE+Style.BRIGHT,memory[4][i],end="         ")
                                names.append(memory[4][i])
                            for i in memory[4]:
                                for i in range(random.randint(4,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                                
                        elif syntax[1] == names_memory[5]:
                            for i in range(len(memory[5])):
                                print(Fore.BLUE+Style.BRIGHT,memory[5][i],end="         ")
                                names.append(memory[5][i])
                            for i in memory[5]:
                                for i in range(random.randint(4,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                                
                        elif syntax[1] == names_memory[6]:
                            for i in range(len(memory[6])):
                                print(Fore.BLUE+Style.BRIGHT,memory[6][i],end="         ")
                                names.append(memory[6][i])
                            for i in memory[6]:
                                for i in range(random.randint(4,7)):
                                    gendir.append(str(random.choice(dirs)))
                                dir.append(list(gendir))
                                gendir.clear()
                        
                        if bonus_chance > 8:
                            file.append(str(files[0]))
                            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
                        if codexprg_chance >= 17:
                            file.append(str(files[6]))
                            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[6],end="         ")
                        if kernelcodeprg_chance >= 17:
                            file.append(str(files[7]))
                            print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[7],end="         ")
                        if easter_chance > 14:
                            file.append(str(files[1]))
                            print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")                      
                        if unknown_chance > 8:
                            file.append(str(files[5]))
                            print(Fore.RED+Style.BRIGHT,files[5],end="         ")
                        if readme_chance > 10:
                            readmenum = random.randint(1,3)
                            if readmenum == 1:
                                file.append(str(files[2]))
                                print(Fore.WHITE+Style.NORMAL,files[2],end="         ")   
                            elif readmenum == 2:
                                file.append(str(files[2]))
                                file.append(str(files[3]))
                                print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                                print(Fore.WHITE+Style.NORMAL,files[3],end="         ")
                            elif readmenum == 3:
                                file.append(str(files[2]))
                                file.append(str(files[3]))
                                file.append(str(files[4]))
                                print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                                print(Fore.WHITE+Style.NORMAL,files[3],end="         ")
                                print(Fore.WHITE+Style.NORMAL,files[4],end="         ")     
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
                        print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                    
            if inp == files[0]:
                if inp == "bonus" and syntax[0] in file: #bonus
                    bonusscore = random.choice(bonuses)
                    print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                    score+=bonusscore
                    file.remove("bonus")
                        
            if inp == files[1]:
                if inp == "easteregg" and syntax[0] in file: #easteregg
                    print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10000 pts",end="         ")
                    score+=10000
                    file.remove("easteregg")
                    
            if inp == "cat "+str(files[2]):
                if files[2] in file:  #readme files
                    if not readme:
                        if kernelread==False:
                            kernelcode_chance = random.randint(1,20)
                        if codexread==False:
                            codex_chance = random.randint(1,20)    
                        bonus_chance = random.randint(1,15)
                        readmescore = random.randint(1,15)
                        
                        if kernelcode_chance == 20 and kernelsolved==False:
                            if kernelread == False:
                                print(specialreadmetexts[0],end=" ")
                                for i in range(3):
                                    kernelcode=random.randint(111,999)
                                print(kernelcode,end="")
                                readme.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                                kernelread=True
                                kernelcode_chance = 0
                                
                        elif codex_chance == 20 and codexsolved==False:
                            if codexread == False:
                                codex = dict(random.sample(list(latinnums.items()), 3))
                                print(specialreadmetexts[1])
                                print(*codex.keys(), end="")
                                readme.append(str(specialreadmetexts[1]))
                                readme.append("".join(codex.keys()))
                                codexnum = list(codex.values())
                                codexread=True
                                codex_chance = 0
                                
                        elif bonus_chance == 15:
                            bonusscore = random.choice(bonuses)
                            print(specialreadmetexts[2],end="")
                            print(bonusscore)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                            score+=bonusscore
                            readme.append(str(specialreadmetexts[2]+str(bonusscore)))
                            
                        elif readmescore >= 13:
                            readme.append(specialreadmetexts[3]+str(score))
                            print(*readme,end="")
                            
                        elif kernelcode_chance  != 20 or codex_chance != 20 or bonus_chance != 15 or readmescore < 13 or kernelsolved == True or codexsolved == True:
                            readme.append(str(random.choice(readmetexts)))
                            print(*readme,end="\r")
                    else:
                        print(*readme,end="\r")
                        
            if inp == "cat "+str(files[3]):
                if files[3] in file:
                    if not readme2:
                        if kernelread==False:
                            kernelcode_chance = random.randint(1,20)
                        if codexread==False:
                            codex_chance = random.randint(1,20)    
                        bonus_chance = random.randint(1,15)
                        readmescore = random.randint(1,15)
                        
                        if kernelcode_chance == 20:
                            if kernelread == False:
                                print(specialreadmetexts[0],end=" ")
                                for i in range(3):
                                    kernelcode=random.randint(111,999)
                                print(kernelcode,end="")
                                readme2.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                                kernelread=True
                                kernelcode_chance = 0
                                
                        elif codex_chance == 20:
                            if codexread == False:
                                codex = dict(random.sample(list(latinnums.items()), 3))
                                print(specialreadmetexts[1])
                                print(*codex.keys(), end="")
                                readme2.append(str(specialreadmetexts[1]))
                                readme2.append("".join(codex.keys()))
                                codexnum = list(codex.values())
                                codexread=True
                                codex_chance = 0
                        
                        elif bonus_chance == 15:
                            bonusscore = random.choice(bonuses)
                            print(specialreadmetexts[2],end="")
                            print(bonusscore)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                            score+=bonusscore
                            readme2.append(str(specialreadmetexts[2]+str(bonusscore)))
                        
                        elif readmescore >= 13:
                            readme2.append(specialreadmetexts[3]+str(score))
                            print(*readme2,end="")
                        
                        elif kernelcode_chance  != 20 or codex_chance != 20 or bonus_chance != 15 or readmescore < 13 or kernelsolved == True or codexsolved == True:
                            readme2.append(str(random.choice(readmetexts)))
                            print(*readme2,end="\r")
                    else:
                        print(*readme2,end="\r")
                        
            if inp == "cat "+str(files[4]):
                if files[4] in file:
                    if not readme3:
                        if kernelread==False:
                            kernelcode_chance = random.randint(1,20)
                        if codexread==False:
                            codex_chance = random.randint(1,20)    
                        bonus_chance = random.randint(1,15)
                        readmescore = random.randint(1,15)
                        
                        if kernelcode_chance == 20:
                            if kernelread == False:
                                print(specialreadmetexts[0],end=" ")
                                for i in range(3):
                                    kernelcode=random.randint(111,999)
                                print(kernelcode,end="")
                                readme3.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                                kernelread=True
                                kernelcode_chance = 0
                                
                        elif codex_chance == 20:
                            if codexread == False:
                                codex = dict(random.sample(list(latinnums.items()), 3))
                                print(specialreadmetexts[1])
                                print(*codex.keys(), end="")
                                readme3.append(str(specialreadmetexts[1]))
                                readme3.append("".join(codex.keys()))
                                codexnum = list(codex.values())
                                codexread=True
                                codex_chance = 0
                        
                        elif bonus_chance == 15:
                            bonusscore = random.choice(bonuses)
                            print(specialreadmetexts[2],end="")
                            print(bonusscore)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                            score+=bonusscore
                            readme3.append(str(specialreadmetexts[2]+str(bonusscore)))
                        
                        elif readmescore >= 13:
                            readme3.append(specialreadmetexts[3]+str(score))
                            print(*readme3,end="")
                            
                        elif kernelcode_chance  != 20 or codex_chance != 20 or bonus_chance != 15 or readmescore < 13 or kernelsolved == True or codexsolved == True:
                            readme3.append(str(random.choice(readmetexts)))
                            print(*readme3,end="\r")
                    else:
                         print(*readme3,end="\r")
                         
            if inp == files[5]:
                crash_chance = random.randint(1,15)
                bonus_chance = random.randint(1,15)
                if inp == "unknown" and syntax[0] in file:
                    wait = time.time() + 0.5
                    while time.time() < wait:
                        print(".",end="", flush=True)
                        time.sleep(0.003)
                    if crash_chance < 12:
                        if bonus_chance >= 14:
                            print("\n")
                            bonusscore = random.choice(bonuses)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                            score+=bonusscore
                            file.remove("unknown")
                                
                        elif bonus_chance < 14:
                            file.remove("unknown")
                            
                    elif crash_chance == 12:
                        layer=0
                        print("\nplayer@termadventure $ ", end="")
                        time.sleep(0.1)
                        print("sudo rm -rf /* --no-preserve-root")
                        time.sleep(0.4)
                        if sys.platform == "win32":
                            os.system("cls")
                        elif sys.platform == "linux":
                            os.system("clear")
                        time.sleep(1)
                        print(Fore.RED+Style.BRIGHT,"* "+Fore.WHITE+Style.NORMAL+"Game over!")
                        time.sleep(2)
                        print(Fore.GREEN,"*"+Fore.WHITE,"Total points collected: "+str(score))
                        time.sleep(2)
                        inp = input("* Do you want to play again or quit the game? (y/n) ")
                        if inp == "n":
                            quit()
                        elif inp == "y":
                            score = 0
                            break
                        
            if inp == files[6]:
                if files[6] in file:
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
                            print("codicem invalidum",end="\n")
                    print("""               ___
gratulationes! XXX punctorum""")
                print("codex: +30000 pts")
                score+=30000
                codexsolved=True
                codexread=False
                codexprg_chance = 0
                file.remove("codex")
                    
            if inp == files[7]:
                if files[7] in file:
                    print(Fore.GREEN,"*"+Fore.WHITE,"Kernel code check ")
                    while True:
                        inp = input("> ")
                        if inp == str(kernelcode):
                            break
                        else:
                            print(Fore.RED,"*"+Fore.WHITE,"Incorrect code")
                    print("kernelcode: +20000 pts")
                score+=20000
                kernelsolved=True
                kernelread=False
                kernelcodeprg_chance = 0
                file.remove("kernelcode")
                    
        if wentbackempty == True and inemptydir == False:
            print(Style.RESET_ALL)
            inp = input("player@termadventure $ ")
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
                        if codexread==True:
                            codexprg_chance = random.randint(1,20)
                        if kernelread==True:
                            kernelcodeprg_chance = random.randint(1,20)
                            
                        print(Fore.GREEN+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer),end="  ")
                        if empty_chance < 7:
                            if syntax[1] == names[0]: #if name[x] print dir[x]
                                if "empty" not in dir[0]:
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
                                    for i in range(len(memory[0])):
                                        print(Fore.BLUE+Style.BRIGHT,memory[0][i], end="         ")
                                        names.append(memory[0][i])
                                        for i in names:
                                            for i in range(random.randint(4,7)):
                                                gendir.append(str(random.choice(dirs)))
                                            dir.append(list(gendir))
                                            gendir.clear()
                                else:
                                    print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                                    inemptydir=True
                            elif syntax[1] == names[1]:
                                if "empty" not in dir[1]:
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
                                    for i in range(len(memory[1])):
                                        print(Fore.BLUE+Style.BRIGHT,memory[1][i], end="         ")
                                        names.append(memory[1][i])
                                        for i in names:
                                            for i in range(random.randint(4,7)):
                                                gendir.append(str(random.choice(dirs)))
                                            dir.append(list(gendir))
                                            gendir.clear()
                                else:
                                    print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                                    inemptydir=True
                            elif syntax[1] == names[2]:
                                if "empty" not in dir[2]:
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
                                    for i in range(len(memory[2])):
                                        print(Fore.BLUE+Style.BRIGHT,memory[2][i], end="         ")
                                        names.append(memory[2][i])
                                        for i in names:
                                            for i in range(random.randint(4,7)):
                                                gendir.append(str(random.choice(dirs)))
                                            dir.append(list(gendir))
                                            gendir.clear()
                                else:
                                    print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                                    inemptydir=True
                            elif syntax[1] == names[3]:
                                if "empty" not in dir[3]:
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
                                    for i in range(len(memory[3])):
                                        print(Fore.BLUE+Style.BRIGHT,memory[3][i], end="         ")
                                        names.append(memory[3][i])
                                        for i in names:
                                            for i in range(random.randint(4,7)):
                                                gendir.append(str(random.choice(dirs)))
                                            dir.append(list(gendir))
                                            gendir.clear()
                                else:
                                    print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                                    inemptydir=True
                            elif syntax[1] == names[4]:
                                if "empty" not in dir[4]:
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
                                    for i in range(len(memory[4])):
                                        print(Fore.BLUE+Style.BRIGHT,memory[4][i], end="         ")
                                        names.append(memory[4][i])
                                        for i in names:
                                            for i in range(random.randint(4,7)):
                                                gendir.append(str(random.choice(dirs)))
                                            dir.append(list(gendir))
                                            gendir.clear()
                                else:
                                    print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                                    inemptydir=True
                            elif syntax[1] == names[5]:
                                if "empty" not in dir[5]:
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
                                    for i in range(len(memory[5])):
                                        print(Fore.BLUE+Style.BRIGHT,memory[5][i], end="         ")
                                        names.append(memory[5][i])
                                        for i in names:
                                            for i in range(random.randint(4,7)):
                                                gendir.append(str(random.choice(dirs)))
                                            dir.append(list(gendir))
                                            gendir.clear()
                                else:
                                    print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                                    inemptydir=True
                            elif syntax[1] == names[6]:
                                if "empty" not in dir[6]:
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
                                    for i in range(len(memory[6])):
                                        print(Fore.BLUE+Style.BRIGHT,memory[6][i], end="         ")
                                        names.append(memory[6][i])
                                        for i in names:
                                            for i in range(random.randint(4,7)):
                                                gendir.append(str(random.choice(dirs)))
                                            dir.append(list(gendir))
                                            gendir.clear()
                                else:
                                    print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                                    inemptydir=True
                                
                            if inemptydir == False:
                                if bonus_chance > 8:
                                    file.append(str(files[0]))
                                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[0],end="         ")
                                if codexprg_chance >= 17:
                                    file.append(str(files[6]))
                                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[6],end="         ")
                                if kernelcodeprg_chance >= 17:
                                    file.append(str(files[7]))
                                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT,files[7],end="         ")
                                if easter_chance > 14:
                                    file.append(str(files[1]))
                                    print(Fore.YELLOW+Style.BRIGHT,files[1],end="         ")
                                if unknown_chance > 8:
                                    file.append(str(files[5]))
                                    print(Fore.RED+Style.BRIGHT,files[5],end="         ")
                                if readme_chance > 10:
                                    readmenum = random.randint(1,3)
                                    if readmenum == 1:
                                        file.append(str(files[2]))
                                        print(Fore.WHITE+Style.NORMAL,files[2],end="         ")   
                                    elif readmenum == 2:
                                        file.append(str(files[2]))
                                        file.append(str(files[3]))
                                        print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                                        print(Fore.WHITE+Style.NORMAL,files[3],end="         ")
                                    elif readmenum == 3:
                                        file.append(str(files[2]))
                                        file.append(str(files[3]))
                                        file.append(str(files[4]))
                                        print(Fore.WHITE+Style.NORMAL,files[2],end="         ")
                                        print(Fore.WHITE+Style.NORMAL,files[3],end="         ")
                                        print(Fore.WHITE+Style.NORMAL,files[4],end="         ")     
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
                            print(Fore.YELLOW,"\n *"+Fore.WHITE,"Directory is empty",end="         ")
                            
                        wentbackempty=False
                        
                if inp == "cd .." and wentbackempty == True:
                    print(Fore.YELLOW,"*"+Fore.WHITE,"You can't go back now!",end="         ")
                    
            if inp == "cat "+str(files[2]):
                if files[2] in file:  #readme files
                    if not readme:
                        if kernelread==False:
                            kernelcode_chance = random.randint(1,20)
                        if codexread==False:
                            codex_chance = random.randint(1,20)    
                        bonus_chance = random.randint(1,15)
                        readmescore = random.randint(1,15)
                        
                        if kernelcode_chance == 20 and kernelsolved==False:
                            if kernelread == False:
                                print(specialreadmetexts[0],end=" ")
                                for i in range(3):
                                    kernelcode=random.randint(111,999)
                                print(kernelcode,end="")
                                readme.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                                kernelread=True
                                kernelcode_chance = 0
                                
                        elif codex_chance == 20 and codexsolved==False:
                            if codexread == False:
                                codex = dict(random.sample(list(latinnums.items()), 3))
                                print(specialreadmetexts[1])
                                print(*codex.keys(), end="")
                                readme.append(str(specialreadmetexts[1]))
                                readme.append("".join(codex.keys()))
                                codexnum = list(codex.values())
                                codexread=True
                                codex_chance = 0
                                
                        elif bonus_chance == 15:
                            bonusscore = random.choice(bonuses)
                            print(specialreadmetexts[2],end="")
                            print(bonusscore)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                            score+=bonusscore
                            readme.append(str(specialreadmetexts[2]+str(bonusscore)))
                            
                        elif readmescore >= 13:
                            readme.append(specialreadmetexts[3]+str(score))
                            print(*readme,end="")
                            
                        elif kernelcode_chance  != 20 or codex_chance != 20 or bonus_chance != 15 or readmescore < 13 or kernelsolved == True or codexsolved == True:
                            readme.append(str(random.choice(readmetexts)))
                            print(*readme,end="\r")
                    else:
                        print(*readme,end="\r")
                        
            if inp == "cat "+str(files[3]):
                if files[3] in file:
                    if not readme2:
                        if kernelread==False:
                            kernelcode_chance = random.randint(1,20)
                        if codexread==False:
                            codex_chance = random.randint(1,20)    
                        bonus_chance = random.randint(1,15)
                        readmescore = random.randint(1,15)
                        
                        if kernelcode_chance == 20:
                            if kernelread == False:
                                print(specialreadmetexts[0],end=" ")
                                for i in range(3):
                                    kernelcode=random.randint(111,999)
                                print(kernelcode,end="")
                                readme2.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                                kernelread=True
                                kernelcode_chance = 0
                                
                        elif codex_chance == 20:
                            if codexread == False:
                                codex = dict(random.sample(list(latinnums.items()), 3))
                                print(specialreadmetexts[1])
                                print(*codex.keys(), end="")
                                readme2.append(str(specialreadmetexts[1]))
                                readme2.append("".join(codex.keys()))
                                codexnum = list(codex.values())
                                codexread=True
                                codex_chance = 0
                        
                        elif bonus_chance == 15:
                            bonusscore = random.choice(bonuses)
                            print(specialreadmetexts[2],end="")
                            print(bonusscore)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                            score+=bonusscore
                            readme2.append(str(specialreadmetexts[2]+str(bonusscore)))
                        
                        elif readmescore >= 13:
                            readme2.append(specialreadmetexts[3]+str(score))
                            print(*readme2,end="")
                        
                        elif kernelcode_chance  != 20 or codex_chance != 20 or bonus_chance != 15 or readmescore < 13 or kernelsolved == True or codexsolved == True:
                            readme2.append(str(random.choice(readmetexts)))
                            print(*readme2,end="\r")
                    else:
                        print(*readme2,end="\r")
                        
            if inp == "cat "+str(files[4]):
                if files[4] in file:
                    if not readme3:
                        if kernelread==False:
                            kernelcode_chance = random.randint(1,20)
                        if codexread==False:
                            codex_chance = random.randint(1,20)    
                        bonus_chance = random.randint(1,15)
                        readmescore = random.randint(1,15)
                        
                        if kernelcode_chance == 20:
                            if kernelread == False:
                                print(specialreadmetexts[0],end=" ")
                                for i in range(3):
                                    kernelcode=random.randint(111,999)
                                print(kernelcode,end="")
                                readme3.append(str(specialreadmetexts[0])+" "+str(kernelcode))
                                kernelread=True
                                kernelcode_chance = 0
                                
                        elif codex_chance == 20:
                            if codexread == False:
                                codex = dict(random.sample(list(latinnums.items()), 3))
                                print(specialreadmetexts[1])
                                print(*codex.keys(), end="")
                                readme3.append(str(specialreadmetexts[1]))
                                readme3.append("".join(codex.keys()))
                                codexnum = list(codex.values())
                                codexread=True
                                codex_chance = 0
                        
                        elif bonus_chance == 15:
                            bonusscore = random.choice(bonuses)
                            print(specialreadmetexts[2],end="")
                            print(bonusscore)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                            score+=bonusscore
                            readme3.append(str(specialreadmetexts[2]+str(bonusscore)))
                        
                        elif readmescore >= 13:
                            readme3.append(specialreadmetexts[3]+str(score))
                            print(*readme3,end="")
                            
                        elif kernelcode_chance  != 20 or codex_chance != 20 or bonus_chance != 15 or readmescore < 13 or kernelsolved == True or codexsolved == True:
                            readme3.append(str(random.choice(readmetexts)))
                            print(*readme3,end="\r")
                    else:
                         print(*readme3,end="\r")
             
            if inp == files[5]:
                crash_chance = random.randint(1,15)
                bonus_chance = random.randint(1,15)
                if inp == "unknown" and syntax[0] in file:
                    wait = time.time() + 0.5
                    while time.time() < wait:
                        print(".",end="", flush=True)
                        time.sleep(0.003)
                    if crash_chance < 12:
                        if bonus_chance >= 14:
                            print("\n")
                            bonusscore = random.choice(bonuses)
                            print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                            score+=bonusscore
                            file.remove("unknown")
                                
                        elif bonus_chance < 14:
                            file.remove("unknown")
                            
                    elif crash_chance == 12:
                        layer=0
                        print("\nplayer@termadventure $ ", end="")
                        time.sleep(0.1)
                        print("sudo rm -rf /* --no-preserve-root")
                        time.sleep(0.4)
                        if sys.platform == "win32":
                            os.system("cls")
                        elif sys.platform == "linux":
                            os.system("clear")
                        time.sleep(1)
                        print(Fore.RED+Style.BRIGHT,"* "+Fore.WHITE+Style.NORMAL+"Game over!")
                        time.sleep(2)
                        print(Fore.GREEN,"*"+Fore.WHITE,"Total points collected: "+str(score))
                        time.sleep(2)
                        inp = input("* Do you want to play again or quit the game? (y/n) ")
                        if inp == "n":
                            quit()
                        elif inp == "y":
                            score = 0
                            break
                            
            if inp == files[6]:           
                if files[6] in file:
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
                            print("codicem invalidum",end="\n")
                            print("""               ___
gratulationes! XXX punctorum""")
                print("codex: +30000 pts")
                score+=30000
                kernelsolved=False
                codexprg_chance=0
                file.remove("codex")
                    
            if inp == files[7]:
                if files[7] in file:
                    print(Fore.YELLOW,"*"+Fore.WHITE,"Kernel code check ")
                    while True:
                        inp = input("> ")
                        if inp == str(kernelcode):
                            break
                        else:
                            print(Fore.RED,"*"+Fore.WHITE,"Incorrect code")
                    print("kernelcode: +20000 pts")   
                score+=20000
                codexsolved=False
                kernelcodeprg_chance=0
                file.remove("kernelcode")
                    
            if inp == "bonus" and syntax[0] in file: #bonus
                    bonusscore = random.choice(bonuses)
                    print(Fore.LIGHTGREEN_EX+Style.NORMAL,"* Bonus! +"+str(bonusscore)+" pts",end="         ")
                    score+=bonusscore
                    file.remove("bonus")
                        
            if syntax[0] == "easteregg" and syntax[0] in file: #easteregg
                print(Fore.YELLOW+Style.BRIGHT,"* Easter egg found! +10000 pts",end="         ")
                score+=10000
                file.remove("easteregg")

    print(Fore.MAGENTA+Style.BRIGHT,"/"+Fore.WHITE+Style.NORMAL,str(layer))
    password = random.choice(rootpasswords)
    time.sleep(2)
    print(Fore.MAGENTA+Style.BRIGHT,"root",end="         ")
    print(Style.RESET_ALL,"password")
    time.sleep(1)
    while True:
        syntax.clear()
        inp = input("player@termadventure $ ")
        syntax = inp.split(" ")
        if inp == "cd root":
            print("bash: cd: root: Permission denied")
        if inp == "cat password":
            print("The password for root user is: "+str(password),end="")
            print(Style.DIM,"* Hint: su root",Style.RESET_ALL)
        if inp == "su root":
            time.sleep(0.1)
            prompt = input("Password: ")        
            if prompt == str(password):
                break    
            else:
                print("su: Authentication failure")
    print(Style.DIM,"* Hint: Enter the root directory to finish the game",Style.RESET_ALL)
    while True:
        syntax.clear()
        inp = input(Fore.MAGENTA+Style.BRIGHT+"root"+Style.RESET_ALL+"@termadventure $ ")
        syntax = inp.split(" ") 
        if inp == "cd root":
            break
    chars=["/","@","#","$","%","&","*","!","?","^","~","`","-","_","=","+","|","{","}","[","]",":",";","<",">",",","."]
    for i in range(50):
        print(Fore.MAGENTA+Style.BRIGHT,3*i*str(random.choice(chars)))
        time.sleep(0.02)
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform == "linux":
        os.system("clear")
    print(Style.RESET_ALL)
    time.sleep(1)
    print(Fore.MAGENTA,"*"+Fore.WHITE,"You made it to the end! Congrats!")
    time.sleep(2)
    print(Fore.GREEN,"*"+Fore.WHITE,"Total points collected: "+str(score))
    time.sleep(2)
    inp = input("* Do you want to play again or quit the game? (y/n) ")
    if inp == "n":
        quit()
    elif inp == "y":
        score = 0