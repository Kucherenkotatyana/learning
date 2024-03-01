from abc import ABC
from abc import abstractmethod
import math


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
        print("calc perimeter")


# s = Shape()     # TypeError: Can't instantiate abstract class Shape with abstract methods area, draw, perimeter


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f"Drawing triangle with sides {self.a}, {self.b}, {self.c}")

    def area(self):
        s = (self.a + self.b + self.c) // 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        super().perimeter()
        return self.a + self.b + self.c


triangle = Triangle(10, 10, 10)
print(triangle.perimeter())
# calc perimeter
# 30
