import math
from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        print('Calc perimeter')

    def drag(self):
        print('Basic dragging functionality')

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f'Drawing triangle with sides: '
              f'{self.a}, '
              f'{self.b},'
              f'{self.c}')

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def drag(self):
        super().drag()
        print('Additional actions')

t = Triangle(10, 12, 14)

print(t.perimeter())
t.drag()