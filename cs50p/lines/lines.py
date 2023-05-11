#Pegar o path do arquivo que for testar. Ex: /workspaces/113629649/0_aula/parity.py
import sys

# file doesn't exist => exit
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

try:
    file = open(sys.argv[1])
    file.close()

except FileNotFoundError:
    sys.exit("File does not exist")

count = 0
with open(sys.argv[1]) as file:
    for line in file:
        if line.lstrip().startswith("#") or len(line.lstrip()) == 0:
            pass
        else:
            count += 1

print(count)