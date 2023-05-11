#Package - Ou seja, o Python executa tudo o que estiver na pasta "test_pack" por conta do arquivo __init__.py,
# mesmo que vazio. Para testar, basta rodar no terminal: pytest 0_aula/test_pack

#Teste da função hello (import) do módulo hello (from), dividido em duas categorias: default e com argumento str
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Bruno") == "hello, Bruno"