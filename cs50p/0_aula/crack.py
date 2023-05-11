#Aula Cybersecurity - YouTube
#Link: https://www.youtube.com/watch?v=Kuy4cEXpXEE
#Aplicação para descobrir uma senha de 4 dígitos e as inúmeras possibilidades
#Aplicações: encryption, end-to-end-encryption, diferença de senhas, defesas: bloqueio temporário,
# two-authentication factor; BitLocker (encriptar o HD); Password Manager;

#Caso 3: senha de 4 dígitos alfanuméricos
from string import ascii_letters, digits, punctuation #importar números, letras maiúsculas, minúsculas e pontuações
from itertools import product #iteração

for passcode in product(ascii_letters + digits + punctuation, repeat=4):
    print(*passcode) #esse '*' é só para exibir melhor o resultado do print
#Resultado 78.074.896 variações possíveis (94 x 94 x 94 x 94)
#CTRL + C para interromper a execução -> KeyboardInterrupt

"""
#Caso 2: senha de 4 dígitos alfabéticos
from string import ascii_letters #importar letras maiúsculas e minúsculas
from itertools import product #iteração

for passcode in product(ascii_letters, repeat=4):
    print(*passcode) #esse '*' é só para exibir melhor o resultado do print
#Resultado 7.311.616 variações possíveis (52 x 52 x 52 x 52)

#Caso 1: senha de 4 dígitos numéricos
from string import digits #importar apenas os dígitos para não fazer manualmente
from itertools import product #iteração

for passcode in product(digits, repeat=4):
    print(*passcode) #esse '*' é só para exibir melhor o resultado do print
#Resultado 10.000 variações possíveis (10 x 10 x 10 x 10)

"""