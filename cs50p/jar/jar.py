class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies in the jar. Over capacity.")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Insufficient cookies in the jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity should be non-negative number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n