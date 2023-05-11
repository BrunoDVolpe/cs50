#Aula 5 - Módulo sys. Função para pegar o que o usuário digitou depois de chamar a função.
#Terminal: python name.py (equivalente a argv[0]) Bruno (argv[1])
#Testar digitando python name.py Bruno
import sys
"""
#print("Hello, my name is", sys.argv[1])
"""
"""
#Para ilustrar:
print(sys.argv)
"""
#Se eu não colocar o nome, vai dar erro por não existir a posição [1]
#Lidando com os erros:
"""
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""
# Ou podemos ir simplesmente com condicionais
"""
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too much argments")
else:
    print("Hello, my name is", sys.argv[1])
"""
# Ou podemos ir simplesmente com condicionais
#Condicionas nós por boas práticas testamos o erro e deixamos a parte certa (ou coração do código)
#fora dessa condicional.

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too much arguments")

print("Hello, my name is", sys.argv[1])