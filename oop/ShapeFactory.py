from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

    def perimeter(self):
        return 2 * (self.h + self.w)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # call Rectangle constructor


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r * self.r

    def perimeter(self):
        return 2 * 3.1416 * self.r


class ShapeFactory:
    def create_shape(self, name):
        if name == 'circle':
            r = float(input("Give the Radius: "))
            return Circle(r)
        elif name == 'square':
            s = float(input("Enter side of Square: "))
            return Square(s)
        elif name == 'rectangle':
            h = float(input("Enter Height: "))
            w = float(input("Enter Width: "))
            return Rectangle(h, w)
        else:
            raise ValueError("Unknown shape")


def client():
    shape = ShapeFactory()
    shape_name = input("""Enter the name of Shape:
circle
square
rectangle
""")
    x = shape.create_shape(shape_name)
    print(f"The Area of {shape_name} is: {x.area()}")
    print(f"The Perimeter of {shape_name} is: {x.perimeter()}")


client()
