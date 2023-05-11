

"""
->

-> Lidando com erros:
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

------------------------------------------------------------------------

-> Treino acessando lista de dicionários e pegando valor específico:

students = [
{"name":"Hermione", "house":"Gryffindor", "patronus":"otter"},
{"name":"Harry", "house":"Gryffindor", "patronus":"Cervo"},
{"name":"Ron", "house":"Gryffindor", "patronus":"nao_sei"},
{"name":"Draco", "house":"Slytherin", "patronos":None}
]

for student in students:
    if student["name"] == "Harry":
        print(student["patronus"])


-> Teste de reescrever um arquivo tirando as linhas duplicadas dele:
import csv
new=[]
with open("students_w.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        if row in new:
            pass
        else:
            new.append(row)

with open("students_w.csv", "w") as file:
    writer = csv.writer(file)
    for info in new:
        writer.writerow(info)

#Validando input de 0 a 255
import re
number = input("Number: ")
matches = re.search(r"^(1?\d?\d|2[0-4]?\d|25[0-5])$",number)
if matches:
    print(True)
else:
    print(False)

-> possibilidade de senha 6 caracteres numéricos
from string import digits, ascii_letters, punctuation

for d1 in (digits):
    for d2 in (digits):
        for d3 in (digits):
            for d4 in (digits):
                for d5 in (digits):
                    for d6 in (digits):
                        print(f"{d1} {d2} {d3} {d4} {d5} {d6}")

"""