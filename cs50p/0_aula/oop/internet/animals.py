#Aula OOP - Python Object Oriented Programming (OOP) - For Beginners
#Link: https://www.youtube.com/watch?v=JeznW_7DlB0
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

#Usando a classe Pet
p = Pet("Tim", 19)
p.speak()
#Usando a classe Cat com propriedades da Pet
c = Cat("Bill", 34, "brown")
c.show()
#Usando método de Dog com a "init" de Pet
#Ou seja, como tem inheritance, se não tem Show em dog, ele procurou na "maior" ou "classe menos específica"
#  e exibiu ela.
d = Dog("Jill", 25)
d.show()