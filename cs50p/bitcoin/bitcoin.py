#pip install requests

import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) == 2:
    try:
        buy = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Request error")
    o = response.json()

    #uma biblioteca, dentro de uma biblioteca, dentro de uma biblioteca. Valores das chaves eram bibliotecas.
    rate = o["bpi"]["USD"]["rate_float"]

    #Printar com separador de milhar "," e 4 casas decimais ".4f"
    print(f"${rate*buy:,.4f}")

"""
#Visualização do retorno da API
import json

api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

print(json.dumps(api.json(), indent=2))
"""