from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
#circle is a shape
class circle(shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14*self.r*self.r
    def perimeter(self):
        return 2*3.14*self.r
#square is a shape
class square(shape):
    def __init__(self, a):
        self.a = a
        
    def area(self):
        return self.a*self.a
    def perimeter(self):
        return 4*self.a
#shape factory has shape
class shape_factory():
    def paint_color(self, name):
        pass
    def create_shape(self, name):
        a = float(input("give radius/arm: "))
        return circle(a) if name=="circle" else square(a)
        
class color(ABC):
    @abstractmethod
    def paint(self):
        pass
class red(color):
    def paint(self):
        return "your shape is painted red"
class blue(color):
    def paint(self):
        return "your shape is painted blue"
#color factory has colors
class color_factory():
    def create_shape(self, name):
        pass
    def paint_color(self, color):
        return red() if color == "red" else blue()

class abstract_factory(ABC):
    @abstractmethod
    def paint_color(self, color):
        pass
    @abstractmethod
    def create_shape(self, name):
        pass

class factory():
    def create_factory(self, choice):
        s = shape_factory()
        c = color_factory()
        return s if choice == "shape" else c

class user():    
    f = factory()
    a = 1
    while(a):
        choice = input("give choice: ")
        factory = f.create_factory(choice)
        a = int(input())
        if choice == "shape":
            name = input("give name: ")
            shape = factory.create_shape(name)
            print(f"area: {shape.area()}\nperimeter: {shape.perimeter()}")
        else:
            name = input("enter color: ")
            color = factory.paint_color(name)
            print(color.paint())

user()