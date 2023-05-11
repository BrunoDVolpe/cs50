#Variação 4 - usando walrus operator (operador morsa) -> :=
import re

name = input("What's your name? ").strip()

if matches:= re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")

"""
First attempt - Mostrando as restrições de não usar a Regular Expression
name = input("What's your name? ").strip()
if "," in name:
    last,first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")

#Variação 1 - usando .groups() e distribuindo a tuple em duas variáveis
import re

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")

#Variação 2 - usando .group(n) nas variáveis
import re

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"Hello, {name}")

#Variação 3 - usando .group(n) de forma otimizada direto na variável, concatenando as strings
import re

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")
"""