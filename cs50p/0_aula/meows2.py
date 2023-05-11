#Exemplo 4
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default="1", help="Number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")

"""
#Exemplo 3
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="Number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

#chamar a função como python meows2.py -h e ver o retorno. Comparar com a descrição do exemplo 2

#Exemplo 2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

#chamar a função como python meows2.py -h e ver o retorno. Comparar com a descrição do exemplo 3

#Exemplo 1 - meows com 'sys'
import sys

if len(sys.argv) == 1:
    print("meow")

elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")

else:
    print("usage: meows2.py")
"""