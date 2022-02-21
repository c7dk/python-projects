class parent:
    pass

class child(parent):
    pass

# ------------------------

class QuadriLateral:
    def __init__(self, a, b, c, d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

class Rectangle(QuadriLateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)

    def area(self):
        return self.side1 * self.side2

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def area(self):
        return self.side1 ** 2


s1 = Square(3)
print(s1.perimeter())
print(s1.side1)
print(s1.area())
