#!/usr/bin/python
# -*- coding: utf-8 -*-

"""collor: Echoes in color  ."""

__author__      = "Leandro Abelin Noskoski"
__site__	= "www.alternativalinux.net"
__projectpage__ = "https://github.com/noskoski/collor"
__copyright__   = "Copyright 2019, Alternativa Linux"
__license__ 	= "GPL"
__version__ 	= "1.1"
__maintainer__ 	= "Leandro Abelin Noskoski"
__email__ 	= "leandro@alternativalinux.net"
__status__ 	= "Production"

import sys, re, random

i = 1
attrange = [0] + range(7 , 0, -1)
fgrange = range(30, 37 + 1) + range(90,97 + 1) + [39]
args = []

def print_usage():
    print("""
Usage: collor.py [ options ..]  colorizetext1 colorizetext2 colorizetext3 ...

Examples:
    cat /var/log/syslog | collor.py  colorizetext1 colorizetext2 colorizetext3
    tail -f /var/log/syslog | collor.py -r colorizetext1 colorizetext2 colorizetext3

Options:
    -r              Randomize colors
    -h or --help    This Message


Version: """ + __version__ + """
""")

##MAIN

if len(sys.argv) <2  or ("-h" in sys.argv) or ("--help" in sys.argv) :
    print_usage()
    sys.exit(1)

if "-r" in sys.argv:
    random.shuffle(fgrange)
    random.shuffle(attrange)

for att in attrange:
    for clfg in fgrange :
        if i < len(sys.argv):
            if not re.match("^-r$",sys.argv[i]):
                args.append([sys.argv[i],clfg,att])
        else:
            break
        i = i + 1

for line in sys.stdin.readlines():
    for arg in args:
        line = re.sub(arg[0],'\033[' + str(arg[2]) + ';'+str(arg[1])+'m' + arg[0] +  '\033[0m', line)
    sys.stdout.write(line)
