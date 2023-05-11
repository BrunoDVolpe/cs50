#Exemplo 10 - Escrita de arquivo inserin-os com dicionários, o que ajuda a não depender da ordem das informações,
#  mas sim de suas colunas.
#Escrita de arquivo. Exemplos com students_w.csv - nele coloquei antes só a primeira linha com o título das colunas.
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_w.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})

"""
#Leituera de arquivo. Exemplos com students.csv e students_d.csv
import csv

students = []
with open("students_d.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key = lambda student: student['name']):
	print(f"{student['name']} is from {student['home']}")
"""


"""
# Exemplo 1: Listar os alunos e suas casas
with open("students.csv", "r") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# Exemplo 2: Listar os alunos e suas casas mudando row por duas variáveis e em ordem alfabética
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(,)
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
#OBS: temos sorte pela frase começar com o nome do aluno. Por isso precisamos de uma maneira mais eficiente de
#  trabalhar os dados. Por isso, usaremos dicionário.

# Exemplo 3: Printar os alunos e suas casas através de dicionário
students = []
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

# Exemplo 4: Printar os alunos e suas casas através de dicionário, criando o dicionário de uma vez.
students = []
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


# Exemplo 5: Printar com nomes em ordem alfabética decrescente (ou das casas se mudar a função em key)
students = []
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

def get_name(students):
    #sorted tem argumento key para receber parâmetro de como ordenar o dicionário
    #key (Optional). A Function to execute to decide the order. Default is None.
    return students["name"]

#Ou função para house:
def get_house(students):
    return students["house"]

for student in sorted(students, key = get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

# Exemplo 6: Anterior, usando a função lambda
students = []
with open("students.csv", "r") as file:
	for line in file:
		name, house = line.rstrip().split(",")
		student = {"name": name, "house": house}
		students.append(student)

for student in sorted(students, key = lambda student: student['name']):
	print(f"{student['name']} is in {student['house']}")

# Exemplo 7: Alteramos students e colocamos "home", onde no Harry tem um com vírgula. Usamos o csv.reader pois na
# função existem recursos para lidar com os corner cases
import csv
students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house, home in reader:
        students.append({"name": name, "house": house, "home": home})

for student in sorted(students, key = lambda student: student['name']):
	print(f"{student['name']} is in {student['house']} and is from {student['home']}")

#Exemplo 8 - Trabalhando direto com dicionário, associando a primeira linha do csv como nome das colunas.
import csv
students = []
with open("students_d.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key = lambda student: student['name']):
	print(f"{student['name']} is from {student['home']}")


#Exemplo 9 - Escrita de arquivo com input e inserindo com lista
#Escrita de arquivo. Exemplos com students_w.csv - nele coloquei antes só a primeira linha com o título das colunas.
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_w.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

#Exemplo 11 - Manipulando imagens. Peguei um cachorro como exemplo.

"""