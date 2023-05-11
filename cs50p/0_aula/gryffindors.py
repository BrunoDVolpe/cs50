#Exemplo enumerate (usando enumerate)
students = ["Harry", "Hermione", "Ron"]

for i, student in enumerate(students, start = 1):
    print(i, student)


"""
#Exemplo enumerate (sem usar enumerate)
students = ["Harry", "Hermione", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])


#Exemplo dictionary comprehension
students = ["Harry", "Hermione", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)


#Exemplo dictionary comprehension (simples, sem usar o dictionary comprehension)
students = ["Harry", "Hermione", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
#gryffindors = [{"name": student, "house": "Gryffindors"} for student in students] #Se fosse list comprehension

print(gryffindors)


#Exemplo usando filter e list comprehension (com lambda para evitar uma função só com retorno)
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

#for gryffindor in gryffindors:
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

#Exemplo usando filter e list comprehension
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

#for gryffindor in gryffindors:
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

#Exemplo usando list comprehension com for e if
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for student in sorted(gryffindors):
    print(student)
"""