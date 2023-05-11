#Exemplo usando uma biblioteca própria chamada sayings.py

import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

"""
#Exemplo com cowsay

# pip install cowsay
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, my name is " + sys.argv[1])
    #cowsay.trex("Hello, my name is " + sys.argv[1])

#Rodar no terminal: python say.py Bruno
"""