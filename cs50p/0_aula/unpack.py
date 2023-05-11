def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {
    "galleons": 100,
    "sickles": 50,
    "knuts": 25,
}

#print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts") #verbose
print(total(**coins)) #É o equivalente a galleons=100, sickles=50, knuts=25
#print(*coins.values()) #também funciona. Descobri sozinho.

## ---------------------------------------
"""
#Exemplo passando nome para as variáveis - (poderia ser um dicionário, não?!)
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

#print(total(*coins), "Knuts")
print(total(galleons=100, sickles=50, knuts=25), "Knuts")

## ---------------------------------------
#Exemplo usando unpacking numa lista
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

#print(*coins)
print(total(*coins), "Knuts")

## ---------------------------------------
#Exemplo passando todos os elementos de uma lista
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
#Esse exemplo é bem "ruim" na escrita. Seria melhor poder passar a lista uma vez. Muito "verbose"
"""