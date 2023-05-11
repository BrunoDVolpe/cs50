#Exemplo de validação com biblioteca 're' - Regular Expressions
import re

email = input("What's your email? ")

if re.search(r"^[a-zA-Z0-9_]+@(\w+\.)?\w+\.edu$",email, re.IGNORECASE): #deixei \w e [a-z...] como exemplos
    print("Valid")
else:
    print("Invalid")

"""
#Exemplo de validação de padrão de forma manual
email = input("What's your email? ").strip().lower()

username, domain = email.split("@")

if username and domain.endwith(".edu"): #if username -> se tiver algum caractere na variável username, verdadeiro.
#                                       & domain terminar com ".edu", verdadeiro.
#                             Porém o usuário ainda pode colocar um e-mail falso, aí teríamos que ter mais validadores.
    print(True)
else:
    print(False)
"""