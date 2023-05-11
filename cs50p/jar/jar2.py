# Fazendo de novo o exercício, sem pegar o frame dele.
class Jar:
    def __init__(self, capacity = 12):
        self._capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1 or not isinstance(capacity, int):
            raise ValueError("Capacity must be and integer bigger than 0")
        if capacity < self.size:
            raise ValueError("Capacity cannot be smaller than actual size")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size bigger than capacity")
        self._size = size

    def deposit(self, cookies):
        if self.size + cookies > self.capacity:
            raise ValueError("Too many cookies in the jar")
        self.size = self.size + cookies

    def withdraw(self, cookies):
        print("nom nom nom")
        if self.size - cookies < 0:
            raise ValueError("Not enought cookies")
        self.size = self.size - cookies

def main():
    #tentando corrigir o erro de capacity e size foi!
    jar = Jar()
    jar.deposit(12)
    #jar.capacity = 10
    jar.deposit(12)
    print("Capacity:", jar.capacity)
    print("Cookies:", jar.size)
    print(jar)

if __name__ == "__main__":
    main()