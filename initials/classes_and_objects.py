class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def addWidth(self, amount):
        self.width += amount

    def addHeight(self, amount):
        self.height += amount


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def addSize(self, amount):
        self.addWidth(amount)
        self.addHeight(amount)


rec1 = Rectangle()
rec1.addWidth(3)

sqr1 = Square(2)
sqr1.addSize(4)

print(vars(rec1))
print(vars(sqr1))
