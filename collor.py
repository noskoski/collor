#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""collor: Echoes in color  ."""

__author__      = "Leandro Abelin Noskoski"
__site__	= "www.alternativalinux.net"
__projectpage__ = "https://github.com/noskoski/collor"
__copyright__   = "Copyright 2019, Alternativa Linux"
__license__ 	= "GPL"
__version__ 	= "2.0"
__maintainer__ 	= "Leandro Abelin Noskoski"
__email__ 	= "leandro@alternativalinux.net"
__status__ 	= "Production"

import sys, re, random

i = 1
attrange = [0] + list(range(7 , 0, -1))
fgrange = list(range(30, 37 + 1)) + list(range(90,97 + 1)) + [39]
args = []

def print_usage():
    print("""
Usage: collor.py [ options ..]  colorizetext1 colorizetext2 colorizetext3 ...

Examples:
    cat /var/log/syslog | collor.py  colorizetext1 colorizetext2 colorizetext3
    tail -f /var/log/syslog | collor.py -r colorizetext1 colorizetext2 colorizetext3

Options:
    -r              Randomize colors
    -o              Only print Matches
    -h or --help    This Message
    -s              Colorize similars ( colorize equal words with same random color )


Version: """ + __version__ + """
""")



class item:
    def __init__(self,nome=None,fg=None,att=None):
        self.nome = nome
        self.fg = random.choice(fgrange)
        self.att = random.choice(attrange)
        self.qtd = 1
        self.cnome = '\033[' + str(self.att) + ';' + str(self.fg) + 'm' + str(self.nome) +  '\033[0m'

    def print(self):
        return("nome:" + str(self.cnome) + " fg:" + str(self.fg) + " att:" + str(self.att) + " qtd:" + str(self.qtd))



class db:
    def __init__(self, min):
        self.words = []
        self.min = min

    def add(self, _str, ign=None):
        if ign:
            splited_str = _str.split();
            for slice in splited_str:
                if len(slice) >= self.min :
                    tt = self.check(slice)
                    if not tt:
                        #sys.stdout.write(slice )
                        _i = item(slice)
                        _str = re.sub(re.escape(slice),_i.cnome,_str, flags=re.IGNORECASE)
                        self.words.append(_i)
                    else:
                        _str = re.sub(re.escape(slice),self.words[tt].cnome,_str, flags=re.IGNORECASE)
        sys.stdout.write(_str )

    def stats(self):
        for y in self.words:
            sys.stdout.write(str(self.words.index(y)) + " = " +   y.print() + "\n")

    def check(self,nome):
        for _x in self.words:
           if _x.nome == nome:
               _x.qtd += 1
               return(self.words.index(_x))
####################################3

if __name__ == '__main__':


    if len(sys.argv) <2  or ("-h" in sys.argv) or ("--help" in sys.argv) :
        print_usage()
        sys.exit(1)

    if "-r" in sys.argv:
        random.shuffle(fgrange)
        random.shuffle(attrange)

    colordb = db(3)

    for att in attrange:
        for clfg in fgrange :
            if i < len(sys.argv):
                if (not re.match("^-r$",sys.argv[i]) ) and (not re.match("^-o$",sys.argv[i]) ) and (not re.match("^-s$",sys.argv[i]) ):
                    args.append([sys.argv[i],clfg,att])
            else:
                break
            i = i + 1

    for line in sys.stdin:
        _have=0
        for arg in args:
            if None != re.match("(.*)" + re.escape(arg[0]) + "(.*)",line,re.M|re.I):
                _have=1
            line = re.sub(re.escape(arg[0]),'\033[' + str(arg[2]) + ';'+str(arg[1])+'m' + arg[0] +  '\033[0m', line)

        if "-s" in sys.argv:
            _s=True
        else:
            _s=False

        if "-o" in sys.argv:
            if _have == 1 :
                colordb.add(line,_s)
        else:
            colordb.add(line,_s)
