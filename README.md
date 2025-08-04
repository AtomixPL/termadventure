# TermAdventure
A small Python console game where you travel through a lot of directories and find various things.

This is my second Python game and it's based on the original ProgressDOS minigame from Progressbar95. It's slightly different and it makes you feel you're exploring an Linux system. This game took me about 1 month to create from my knowledge of Python (sometimes i needed chatgpt). All you need to do is to collect as many bonuses as you can while exploring directories. You can also find codes inside readme files for various code programs, which can give you a lot of points. To finish the game, you need to get to the 50th directory. The game is in Alpha, so many features are missing and the game is still work in progress.
## Navigating the system
While exploring the system **you cannot go back by one directory** until you will find an empty one. Remember to always claim bonuses when you'll encounter them, otherwise they will be gone.
### Available commands
_ls_ - list directories

_cd (dir)_ - change directory

_cd .._ - leave the directory

_cat (text file)_ - read the content of the text file

_(executable)_ - run the program or claim bonus

_su root_ - switch to the root user (if you know the password)
## Bonuses, eastereggs and unknown files
Bonuses are common executables that can give you from 1 000 to 5 000 points. Eastereggs are less common, and they are worth 10 000 points. However unknown files are more dangerous, they can ~~steal your points or~~ delete your whole system, and this is where the game ends. But rarely they can give you some points.
## Readme files
Inside those text files there are random contents written, but you can encounter mysterious codes, which can hint to more worthy and interesting programs, that can contain up to 100 000 points. They can only appear after finding such codes.
## Kernelcode, chroma, codex and hex
Kernelcode is an executable where you must type in correct 3-digit code which you can find in the text file beginning with the Linux kernel version. By successfully solving the program you can get 20 000 points. Another special program is Chroma, which is an alternative to kernelcode, and it needs a special six-letter color code, which you can also find in one of the readme files. You will get awarded 30 000 points for the solve. Codex is an extrordinary latin program, which works the same as kernelcode, but you need to know numbers in latin. When you'll encounter a readme file with "lorem ipsum" text inside it, there are numbers written in latin below, eg. unus, duo, tres etc. By correctly typing the 3-digit code as in kernelcode you can get 50 000 points. The last and the hardest of the four programs is Hex, where you must find five reiterations of the same hex number in a grid of those numbers. Be aware, that you must complete it three times, and after finding the number the grid becomes larger, and it will be harder to find the correct number. If you manage to find those numbers, the award is 100 000 points. After solving all of the four special programs, you get an extra bonus of 200 000 points.
## Changelog
0.1 (08-07-2025) - initial release

0.2 (09-07-2025) - added loading screen

0.3 (02-08-2025) - added automatic module installation needed to run the game

0.4 (03-08-2025) - the game can be now ran as an executable and new special program Chroma

0.5 (04-08-2025) - new special program Hex, revamped game over screen and minor improvements
