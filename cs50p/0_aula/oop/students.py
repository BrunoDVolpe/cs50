class Student:
    def __init__(self, name, house):
        #__init__ roda apenas na primeira vez que criamos o objeto.
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            #é o mesmo que if name == "":
            raise ValueError("Missing name")
        self._name = name

    #getter
    @property
    def house(self):
        return self._house #tecnicamente estamos chamando estância de _house e a propriedade de house

    #setter
    @house.setter
    def house(self, house):
        #Como init só roda uma vez, poderíamos trocar o nome de house e não teríamos mais a validação.
        #Por isso colocamos aqui no setter a condição. No setter, ela roda toda vez que a variável
        #for chamada, mesmo no __init__
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
#    student.house = "Number Four, Private Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) #constructor


if __name__ == "__main__":
    main()

"""
# Antes de colocar a validação de student e com as anotações:
#Retomando do 1:21:47 para relembrar o que fiz abaixo e continuar a aula. Neste tempo vai começar a falar da propriedade.
class Student:
    def __init__(self, name, house):
        #__init__ roda apenas na primeira vez que criamos o objeto.
        if not name:
            #é o mesmo que if name == ""
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    #getter
    @property
    def house(self):
        return self._house #tecnicamente estamos chamando estância de _house e a propriedade de house

    #setter
    @house.setter
    def house(self, house):
        #Como init só roda uma vez, poderíamos trocar o nome de house e não teríamos mais a validação.
        #Por isso colocamos aqui no setter a condição. No setter, ela roda toda vez que a variável
        #for chamada, mesmo no __init__
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
#    student.house = "Number Four, Private Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) #constructor


if __name__ == "__main__":
    main()


#Voltando ao exemplo anterior:
Aqui nós temos uma classe "Student" com dois métodos (__init__ and __str__).
O primeiro leva 'self' no primeiro argumento, como sempre será; seguido de mais dois argumentos (name e house)
Validamos o 'name', validamos a 'house' e então atribuímos 'name' e 'house' respectivamente para duas 'instances
 variables' chamadas também de 'name' e 'house', mas usamos 'self' para acessar o objeto atual e armazenar os valores
 dentro dele mesmo.
Temos também o método __str__ que leva um argumento 'self' que é pré-requisito para criar o método e esse método vai
ser automaticamente chamado toda vez que quisermos converter esse student object numa string, como fazemos aqui.

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

#Exemplo criando uma classe própria, diferente das padrões do Python
#Neste exemplo, quando chamarmos a classe Student, criaremos um objeto que representa determinado aluno
#  (no caso do mundo do Harry) e fazê-lo lançar um feitiço.
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        #poderia ser com if else também
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🐳"
            case "Jack Russel Terrier":
                return "🐶"
            case _:
                return "✨"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

#primeiro exemplo com classe
class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()

#Antes de usar classe:
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


#Outra forma de retornar um dicionário.
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()

#Usando Tupla
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

#Usando Tupla
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

#Usando Lista
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]
"""