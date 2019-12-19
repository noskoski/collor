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

import sys, re, random, argparse

i = 1
attrange = [0] + list(range(7 , 0, -1))
fgrange = list(range(30, 37 + 1)) + list(range(90,97 + 1)) + [39]
bgrange = list(range(40, 47 + 1)) + list(range(100,107 + 1)) + [49]
_hi = []

class item:
    def __init__(self,nome=None,fg=None,att=None,bg=None):
        self.nome = nome
        self.fg = random.choice(fgrange)
        self.bg = random.choice(bgrange)
        self.att = random.choice(attrange)
        self.qtd = 1
        self.cnome = '\x1B[' + str(self.att) + ';' + str(self.bg) + ';' + str(self.fg) + 'm' + str(self.nome) +  '\x1B[0m'

    def print(self):
        return("nome:" + str(self.cnome) + " fg:" + str(self.fg) + " bg:" + str(self.bg) + " att:" + str(self.att) + " qtd:" + str(self.qtd))



class db:
    def __init__(self, min, max):
        self.words = []
        self.min = min
        self.max = max

    def add(self, _str, ign=None):
        if ign:
            splitted_str = self._split(_str)
            for slice in splitted_str:
                if len(slice) >= self.min and len(slice) < self.max:
                    tt = self.check(slice)
                    if not tt and not tt == 0:
                        _i = item(slice)
                        _str = re.sub(re.escape(slice),_i.cnome,_str, flags=re.IGNORECASE)
                        self.words.append(_i)
                    else:
                        _str = re.sub(re.escape(slice),self.words[tt].cnome,_str, flags=re.IGNORECASE)
        sys.stdout.write(_str )

    def stats(self):
        for y in self.words:
            sys.stdout.write(str(self.words.index(y)) + " = " +   y.print() + "\n")

    def count(self):
        sys.stdout.write(str(len(self.words)))

    def check(self,nome):
        if '\x1B[' not in nome: ## bypass existent color
            for _x in self.words:
                if  _x.nome == nome:
                    _x.qtd += 1
                    return(self.words.index(_x))
        return(None)

    def _split(self,_str):

        _grp = [""]
        if "S" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('\[.*?\]')
        if "P" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('\(.*?\)')
        if "X" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('\<.*?\>')
        if "Y" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('\{.*?\}')
        if "T" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('[0-2]{0,1}[0-9]{1}\:[0-9]{1,2}\:[0-9]{1,2}')
        if "E" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        if "D" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('[0-9]{2,4}-[0-9]{2}-[0-9]{2,4}')
        if "U" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        if "I" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        if "Q" in args.patterns[0] or "A" in args.patterns[0]:
            _grp.append('"(.*?)"')
            _grp.append('\'(.*?)\'')
        _arr = []
#        print(_grp)
        for _i in _grp :
             _matches = re.findall(_i, _str)
             for _match in _matches:
                   _arr.append(_match)
        return( _arr)



####################################3

if __name__ == '__main__':



    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument("-r", "--random",
                help="set you need random colors",
                action='store_true')
    parser.add_argument("-o", "--only",
                help="print only match strings",
                action='store_true')
    parser.add_argument("-p", "--patterns",
                help="Search for patterns ADTUEIPSXY = \n( A=ALL, D=Date, T=Time, U=Urls, E=Emails, I=Ips, P=(), S=[], X=<>, Y={}, Q=\"\" or '' )",
                metavar='pattern chars',
                type=str,
                nargs='+')
    parser.add_argument("-H", "--highlight",
                help=" word's for highlight",
                metavar='word',
                type=str,
                nargs='+')

    args = parser.parse_args()
    print(args)

#    if len(sys.argv) <2  or ("-h" in sys.argv) or ("--help" in sys.argv) :
#        sys.exit(1)

    if args.random:
        random.shuffle(fgrange)
        random.shuffle(bgrange)
        random.shuffle(attrange)

    colordb = db(1,600)
    i=0

    if ( args.highlight==None and args.only==False and args.patterns==None ):
        args.patterns="A"

    if args.highlight:
        for att in attrange:
            for clbg in bgrange :
                for clfg in fgrange :
                    if i < len(args.highlight):
                            _hi.append([args.highlight[i],clfg,att,clbg])
                    else:
                        break
                    i += 1

    for line in sys.stdin:
        _have=0
        for hi in _hi:
            if None != re.match("(.*)" + re.escape(hi[0]) + "(.*)",line,re.M|re.I):
                _have=1
            line = re.sub(re.escape(hi[0]),'\033[' + str(hi[2]) + ';' + str(hi[3]) + ';' + str(hi[1])+'m' + hi[0] +  '\033[0m', line)

        if args.patterns and len(args.patterns):
            _s=True
        else:
            _s=False

        if "-o" in sys.argv:
            if _have == 1 :
                colordb.add(line,_s)
        else:
            colordb.add(line,_s)
    #colordb.stats()
