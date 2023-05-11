#Exemplo 5: usando list comprehension (múltiplos elementos)
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased) #unpacking all arguments as independent arguments: THIS IS CS50

if __name__ == "__main__":
    main()

"""
#Exemplo 4: usando map (múltiplos elementos)
#Este está perfeito! Faremos exemplo 5 como outra sugestão / outro recurso
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased) #unpacking all arguments as independent arguments: THIS IS CS50

if __name__ == "__main__":
    main()
"""
"""
#Exemplo 3: usando múltiplos argumentos usando *args (múltiplos elementos)
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
#    print(uppercased) #assim printa uma lista. Não é o que queremos: ["THIS", "IS", "CS50"]. Precisamos de unpacking
    print(*uppercased) #unpacking all arguments as independent arguments: THIS IS CS50

if __name__ == "__main__":
    main()

#Exemplo 2: Gritando à partir de uma lista de strings (1 argumento)
def main():
    yell(["This", "is", "CS50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
#    print(uppercased) #assim printa uma lista. Não é o que queremos: ["THIS", "IS", "CS50"]. Precisamos de unpacking
    print(*uppercased) #unpacking all arguments as independent arguments: THIS IS CS50

if __name__ == "__main__":
    main()


#Exemplo 1: gritando à partir de uma frase (1 argumento)
def main():
    yell("This is CS50")

def yell(phrase):
    print(phrase.upper())


if __name__ == "__main__":
    main()
"""