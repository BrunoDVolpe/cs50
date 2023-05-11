#Input do usuário
var = input("Var's name? ")

#Procurar pela letra maiúscula
for char in var:
    if char.islower() or char.isnumeric():
        print(char, end="")
    else:
        print("_", char.lower(), sep="", end="")
print()