# collor
Colorize stdout, make it alot more readable , needs python3

Usage: collor.py [ options ..]  colorizetext1 colorizetext2 colorizetext3  "Expression to colorize" ...

Examples:

    cat /var/log/syslog | collor.py  colorizetext1 colorizetext2 colorizetext3

    tail -f /var/log/syslog | collor.py -r colorizetext1 colorizetext2 colorizetext3

Options:
    -r              Randomize colors
    -o              Only print Matches
    -h or --help    This Message
