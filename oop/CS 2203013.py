from abc import ABC, abstractmethod
# ─────────────────────────────────────────
class AbstractFactory(ABC):
    @abstractmethod
    def create_shape(self, shape_name):
        pass
    @abstractmethod
    def create_color(self, color_name):
        pass
# ─────────────────────────────────────────
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
        super().__init__(side, side)
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.1416 * self.r * self.r
    def perimeter(self):
        return 2 * 3.1416 * self.r
# ─────────────────────────────────────────
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass
class Red(Color):
    def fill(self):
        return "The Shape is Filled with Red"
class Green(Color):
    def fill(self):
        return "The Shape is Filled with Green"
class Blue(Color):
    def fill(self):
        return "The Shape is Filled with Blue"
# ────────────────────────────────────────
class ColorFactory(AbstractFactory):
    def create_shape(self, shape_name):
        return None
    def create_color(self, name):
        if name == 'red':
            return Red()
        elif name == 'green':
            return Green()
        elif name == 'blue':
            return Blue()
        else:
            raise ValueError("Unknown color")
# ─────────────────────────────────────────
class ShapeFactory(AbstractFactory):
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
    def create_color(self, color_name):
        return None
# ─────────────────────────────────────────
class Factory:
    def createFactory(self, choice):
        if choice == "shape":
            return ShapeFactory()
        elif choice == "color":
            return ColorFactory()
        else:
            raise ValueError(print("Invalid Choice"))
# ─────────────────────────────────────────
def client():
    while True:
        choice = input("Choose factory: shape, color, quit: ")
        if choice == "quit":
            print("Exit")
            break
        f = Factory()
        factory = f.createFactory(choice)

        if choice == "shape":
            shape_name = input("Enter the name of Shape: circle, square, rectangle: ")
            x = factory.create_shape(shape_name)
            print(f"The Area of {shape_name} is: {x.area():.4f}")
            print(f"The Perimeter of {shape_name} is: {x.perimeter():.4f}")

        elif choice == "color":
            color_name = input("Enter the color name: red, green, blue: ")
            c = factory.create_color(color_name)
            print(c.fill())


client()