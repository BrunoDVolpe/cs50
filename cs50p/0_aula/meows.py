#pip install mypy
#Exemplo type hints: Mudando para retorno esperado de str e corrigindo erro da impressão de None.
def meow(n: int) -> str:
    """Meow n times."""
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

"""
#pip install mypy
#Exemplo type hints: neste caso sugerimos que a função retorna None e dizemos que esperamos uma str em meows. Erro.
# A função ainda é executada, porém imprime um None no final
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

#pip install mypy
#Exemplo type hints: ele aponta o erro do input (str) como número (int)
def meow(n: int):
    for _ in range(n):
        print("meow")

#number: int = input("Number: ")
number = int(input("Number: "))
meow(number)

#Alternativa usando OOP
class Cat:
    MEOWS = 3 #constant in a sense of "you should not touch there"

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()

#Mostrando que a convenção não garante malandragem
MEOWS = 3

MEOWS = 4 #induzindo o erro e o Python aceita
for _ in range(MEOWS):
    print("meow")
"""