#Dessa forma nós simplificamos a chamada da classe de student = Student(name, house) para student = Student.get().
#  Ele vai chamar o método sem criar um objeto e no return, ele retornará um objeto da classe que está, ou seja, Student,
#  inserindo name e house. Logo, criará um objeto, mas com a chamada mais "didática" da função.
# Relembrando, students.py tinha uma função que chamada inputs e depois criava o objeto. Agora criamos o objeto à partir
# de um método da própria classe Student.

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()