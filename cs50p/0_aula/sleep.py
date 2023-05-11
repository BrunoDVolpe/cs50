#Função com generators | yield - Testar com 100, funciona bem. Com 1.000.000 ele não trava mais.
def main():
    n = int(input("Number: "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐏" * (i)


if __name__ == "__main__":
    main()

"""
#Função sem generators | yield - Testar com 100, funciona bem. Com 1.000.000 ele trava. Se esperar o suficiente aparecerá
#  uma mensagem de 'killed', ele vai interromper por conta da quantidade de memória e CPU requerida para a tarefa.
def main():
    n = int(input("Number: "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = [] #gerar essa lista com 1.000.000 trava o programa
    for i in range(n):
        flock.append("🐏" * i)
    return flock


if __name__ == "__main__":
    main()
"""