class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 6)
print("r1 area=%d, r2 area=%d"%(r1.calculateArea(), r2.calculateArea()))