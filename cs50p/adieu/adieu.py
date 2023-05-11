#pip install inflect
import inflect

# JOIN WORDS INTO A LIST:
#p = inflect.engine()
#mylist = p.join(("apple", "banana", "carrot"))

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(names)}")

"""
#Esse programa eu fiz por conta própria, sem usar o hint ou biblioteca

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")

elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")

elif len(names) > 2:
    print(f"Adieu, adieu, to ", end="")
    for n in names[:-1]:
        print(f"{n}, ", end="")
    print(f"and {names[-1]}")
"""