#Abrir, escrever a variável name e fechar o arquivo. Em "def" para continuar o arquivo.
def Abrir_escrever_fechar():
    name = input("What's your name? ")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")

#Ler o arquivo, ir linha a linha printando "Hello, " + o nome das pessoas em ordem alfabética e fechar o arquivo
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")


"""
#Histórico
#Abrir um arquivo (ou criar se não existir), escrever a variável name e fechar o arquivo (Jeito 1)
name = input("What's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

#(Jeito 2 - Compacto)
name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Ler um arquivo linha por linha, organizar em ordem alfabética, printar com Hello (jeito 1)
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"Hello, {name}")

#(Jeito 2 - compacto)
with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")
"""