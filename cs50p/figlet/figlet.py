#pip install pyfiglet
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fontes = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    f = random.choice(fontes)
    figlet.setFont(font=f)
    print(figlet.renderText(s))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        for font in fontes:
            if font == sys.argv[2]:
                figlet.setFont(font=sys.argv[2])
                s = input("Input: ")
                print(figlet.renderText(s))
                sys.exit()
    sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

"""
Outro jeito, usando "if argument in list[]:"
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fontes = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    f = random.choice(fontes)
    figlet.setFont(font=f)
    print(figlet.renderText(s))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fontes:
            figlet.setFont(font=sys.argv[2])
            s = input("Input: ")
            print(figlet.renderText(s))
        else:
            sys.exit("Invalid usage 3")
    else:
        sys.exit("Invalid usage 2")
else:
    sys.exit("Invalid usage")
"""