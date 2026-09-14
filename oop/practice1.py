from abc import ABC, abstractmethod


# ___________________________
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r * self.r

    def parameter(self):
        return 2 * 3.1416 * self.r


class square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def parameter(self):
        return 4 * self.a


# _________________________________
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass


class red(Color):
    def fill(self):
        return "RED"


class blue(Color):
    def fill(self):
        return "BLUE"


# ________________________________

class AbstractFactory(ABC):
    @abstractmethod
    def create_shape(self, name):
        pass

    @abstractmethod
    def create_color(self, name):
        pass


class shape_factory(AbstractFactory):
    def create_color(self, name):
        pass

    def create_shape(self, name):
        if name == "circle":
            r = float(input("Enter radius: "))
            return Circle(r)
        elif name == "square":
            r = float(input("Enter side: "))
            return square(r)
        else:
            print("invalid input")


class color_factory(AbstractFactory):
    def create_shape(self, name):
        pass

    def create_color(self, name):
        if name == 'red':
            return red()
        elif name == 'blue':
            return blue()
        else:
            raise ValueError("Unknown color")


# __________________________________

class Factory:
    def create_factory(self, choice):
        if choice == "color":
            return color_factory()
        elif choice == "shape":
            return shape_factory()


def client():
    choice = input("select factory: shape, color: ")
    factory = Factory()
    f = factory.create_factory(choice)

    if choice == "shape":
        name = input("Enter shape: circle, square: ")
        x = f.create_shape(name)
        print(f"{name}: {x.area():.3f}")
        print(f"{name}: {x.parameter():.3f}")
    elif choice == "color":
        name = input("Enter color: red, blue: ")
        x = f.create_color(name)


client()
