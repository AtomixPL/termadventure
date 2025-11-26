# TermAdventure
A small Python console game where you travel through a lot of directories and find various things.

This game is based on the original ProgressDOS minigame from Progressbar95. It took me about 1 month to create. All you need to do is to collect as many points as you can while exploring the Linux system. To finish the game, you need to get to the 50th directory, but you will need a password. The game can be launched on Windows and Linux distros.
## Setup
To ensure the proper execution of the game, please run the "build.py" file inside PowerShell or cmd. Make sure you open the file inside console, otherwise build.py will fail to start. It will automatically install necessary modules needed for the game and build the executable file from source code. After that you can play the game by running the compiled executable file from the dist directory.
**Note:** If you are using Ubuntu or Debian based distros, you will have to install python3-venv package in order to run build.py.
## Navigating the system
While exploring the system **you cannot go back by one directory** except when you'll find an empty one. Remember to always claim bonuses when you encounter them, otherwise they will be gone.
### Available commands
_ls_ - list directories

_cd (dir)_ - change directory

_cd .._ - leave the directory

_cat (text file)_ - read the content of the text file

_(executable)_ - run the program or claim bonus
## In-game executables and readme files
Bonus - common executable, points ranging from 1000 to 5000
Easteregg - uncommon executable, 10 000 points
Readme - text files, which can hint to a special program, or give you some points
Unknown - mysterious file, which either does nothing, acts as a Bonus or deletes your in-game system
## Special progams
Kernelcode - simple utility checking for a three-digit code, 20 000 points
Chroma - another code-checking program, which needs a specific color code, 30 000 points
Codex - Kernelcode's extrordinary latin program for a three-digit code from a latin-translated set, 50 000 points
Hex - more advanced utility for checking a hex code iteration in a set, 100 000 points

For solving all of these you can get extra 200 000 points.
## Changelog
v0.1.0-alpha (08-07-2025) - initial release

v0.2.0-alpha (09-07-2025) - added loading screen

v0.3.0-alpha (02-08-2025) - added automatic module installation needed to run the game

v0.4.0-alpha (03-08-2025) - the game can be now ran as an executable and new special program Chroma

v0.5.0-alpha (04-08-2025) - new special program Hex, revamped game over screen and minor improvements

v0.6.0-beta (05-08-2025) - game results are now automatically being saved in json file (scoreboard.json)

v0.7.0-beta (17-09-2025) - added build.py file for user to automatically install dependencies and properly setup the game, scoreboard was removed due to problems with handling game executable, you can now type in your username before starting the game

v0.8.0-beta (20-09-2025) - smaller specprogs chances, smaller unknown crash chance, final layer revamped

v0.9.0-beta (05-10-2025) - chroma screen revamp, fixed genfiles outputting when inemptydir, gendirs and gendirsback code optimized, su root removed, smaller root dir password chance

v1.0.0 (06-10-2025) - fixed hex appearing after completing it, improved hex program, game theme changed, "loading" screen changed, slightly higher passwd_chance

v1.0.1 (06-10-2025) - fixed hex "correct" text overlapping, reverting hex quit option, another hex postsolve appearance fix, new directory names

v1.0.2 (06-10-2025) - small text fix on "no password" scenario on final layer

v1.0.3 (07-10-2025) - typing a blank username is now impossible

v1.0.4 (21-11-2025) - game code was cleaned up and constant game variables were moved to separate file

v1.0.5 (24-11-2025) - game was split into five seperate .py files for organisational purposes