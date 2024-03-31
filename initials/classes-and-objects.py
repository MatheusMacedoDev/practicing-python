class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def addWidth(self, amount):
        self.width += amount

    def addHeight(self, amount):
        self.height += amount


rec1 = Rectangle()
rec1.addWidth(3)

print(vars(rec1))
