#Quarta variação, usando Regular Expression - search
#Sub ainda falhava se o usuário colocar um domínio diferente do twitter.
import re

url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)",url, re.IGNORECASE):
    print("Username:", matches.group(1))

"""
#Primeiro exemplo - Pegar username à partir da URL
url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
#Porém fica muito frágil. Se vier http:// ou www. ou / depois do username ou ? depois do username ou um texto, como
# meu twitter é https://twitter.com/davidjmalan ou alguma outra variação, o programa pegará a informação errada.

#Segunda variação, usando .removeprefix()
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
#Dessa forma, se o input começar com o 'https://twitter.com/', ele vai removê-lo e mostrar apenas o usuário. Se não
# for assim, ele vai retornar o input original.

#Terceira variação, usando Regular Expression - sub
import re

url = input("URL: ").strip()
username = re.sub(r"(^https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

#Quarta variação sem usar Walrus Operator
import re

url = input("URL: ").strip()

matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)",url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))
"""