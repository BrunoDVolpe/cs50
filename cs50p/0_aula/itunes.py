#Vamos usar uma API da Apple que tem 3 parâmetros, o tipo do que vamos pegar (song, no caso),
# entity que representa a quantidade de resultados que o iTunes irá retornar
# e o "term" que representa o nome da banda que ele irá procurar.
#-> https://itunes.apple.com/search?entity=song&limit=1&term=weezer

#pip install requests
import requests
import sys
import json

#Error checking
if len(sys.argv) != 2:
    sys.exit()

#Usar o requests para "fingir" ser um navegador
#response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))

#Me trouxe o resultado de uma música, no formato de dicionário, com dois valores, sendo um dicionários e uma lista
#  de dicionários. Nesta, existe um dicionário com a key "trackName" e o valor "Say It Ain't So", ou seja, o nome
# da música. Sendo assim, posso aumentar o "limit" no link da API para que ele me traga um número maior de músicas
# e, através do for, fazer com que exiba apenas esses nomes, um abaixo do outro.

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
# nome "o" vem de object
o = response.json()

for result in o["results"]:
    print(result["trackName"])