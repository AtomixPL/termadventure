# dynamic.py
# Dynamic variables and tables for TermAdventure
# Copyright (c) 2025 AtomixPL
# Licensed under the GNU General Public License

class Dynamic:
    def initstate(self):
        self.score=0
        self.syntax=0
        self.memory=[]
        self.dir=[]
        self.names=[]
        self.names_memory=[]
        self.gendir=[]
        self.file=[]
        self.file_memory=[]
        self.readme=[]
        self.readme2=[]
        self.readme3=[]
        self.kernelcode=0
        self.codexnum=0
        self.chromacode=0
        self.layer=1
        self.kernelcode_chance=0
        self.codex_chance=0
        self.chroma_chance=0
        self.codexprg_chance=0
        self.kernelcodeprg_chance=0
        self.chromaprg_chance=0
        self.hexprg_chance=0
        self.passwd_chance=0
        self.prgfound=0
        self.bonus_chance=0
        self.easter_chance=0
        self.readme_chance=0
        self.unknown_chance=0
        self.wentbackempty=False
        self.inemptydir=False
        self.kernelread=False
        self.codexread=False
        self.chromaread=False
        self.kernelsolved=False
        self.codexsolved=False
        self.chromasolved=False
        self.hexsolved=False
        self.solvedall=False
        self.passwdfound=False
    
    def __init__(self):
        self.initstate()
    
    def reset(self):
        self.initstate()
        
d = Dynamic()
