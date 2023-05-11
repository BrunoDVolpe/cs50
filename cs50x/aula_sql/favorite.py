import csv
"""
#Exemplo da aula usando csv. Ele pegou do google forms a resposta dos alunos.
with open("Favorite TV Shows - Form Responses.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) #pular a primeira linha já que é só cabeçalho
    for row in reader:
        print(row[1]) #printar valores da coluna 2, que representa o nome das séries

#Exemplo da aula usando DictReader, mais robusto. Separando todos os títulos
titles = set()

with open("Favorite TV Shows - Form Responses.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        titles.add(row['title'].strip().upper()) #printar valores da coluna title, que representa o nome das séries
                            #(agora independe da posição da coluna, o DictReader cuida disso pra mim).
                            # Tornamos ela case insensitive, tirando espaços em branco do começo e fim e deixando em
                            # letra maiúscula

for title in sorted(titles):
    print(title)
"""
"""
#Calcular a quantidade para cada título
titles = {}

with open("Favorite TV Shows - Form Responses.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if title not in titles:
            titles[title] = 0
        titles[title] += 1

def f(title):
    return titles[title]
"""
"""
#Como estou chamando a função várias vezes dentro de key, eu não uso parênteses. Faz parte da lógica de sorted.
for title in sorted(titles, key=f, reverse=True):
    print(title, titles[title])
"""
"""
#Usando lambda para o sorted function
for title in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(title, titles[title])
"""
#Procurar o favorito
title = input("Title: ").strip().upper()

with open("Favorite TV Shows - Form Responses.csv", "r") as file:
    reader = csv.DictReader(file)
    counter = 0
    for row in reader:
        if row["title"].strip().upper() == title:
            counter += 1
print(counter)