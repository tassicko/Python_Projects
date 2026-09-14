from abc import ABC, abstractmethod
import math
from tokenize import endpats

#_________________________________________________
class AbstractFactory(ABC):
    @abstractmethod
    def create_circle(self):
        pass
    @abstractmethod
    def create_square(self):
        pass
    @abstractmethod
    def create_sphere(self):
        pass
    @abstractmethod
    def create_cube(self):
        pass    
#_________________________________________________



#_________________________________________________
class Shape2DFactory(AbstractFactory):
    def create_cube(self):
        pass
    def create_sphere(self):
        pass
    
    def create_circle(self):
        r = float(input("Enter radius: "))
        return Circle2D(r)
    def create_square(self):
        s = float(input("Enter side: "))
        return Square2D(s)

class Shape2D(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle2D(Shape2D):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r
    def perimeter(self):
        return 2 * math.pi * self.r

class Square2D(Shape2D):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
#_________________________________________________



#_________________________________________________
class Shape3DFactory(AbstractFactory):
    def create_circle(self):
        pass
    def create_square(self):
        pass
    def create_sphere(self):
        r = float(input("Enter radius: "))
        return Sphere3D(r)
    def create_cube(self):
        s = float(input("Enter side: "))
        return Cube3D(s)

class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        pass
    @abstractmethod
    def surface_area(self):
        pass

class Sphere3D(Shape3D):
    def __init__(self, r):
        self.r = r
    def volume(self):
        return (4 / 3) * math.pi * self.r ** 3
    def surface_area(self):
        return 4 * math.pi * self.r ** 2

class Cube3D(Shape3D):
    def __init__(self, side):
        self.side = side
    def volume(self):
        return self.side ** 3
    def surface_area(self):
        return 6 * self.side ** 2

#________________________________________________



class Factory:
    def create_factory(self, choice):
        if choice == 1:
            return Shape2DFactory()
        elif choice == 2:
            return Shape3DFactory()


def client():
    f = Factory()
    while True:
        choice = int(input("""Choose Shape Type:   1  |   2   |   3
         1) 2d Shapes 
         2) 3d Shapes
         3) quit
         :                  """))
        if choice == 3:
            break


        factory = f.create_factory(choice)

        if choice == 1:
            shape_name = int(input("""Enter Shape:   1  |   2
            1)circle 
            2)square
            :               """))

            if shape_name == 1:
                x = factory.create_circle()
            elif shape_name == 2:
                x = factory.create_square()

            print(f"Area: {x.area():.3f}")
            print(f"Perimeter: {x.perimeter():.3f}")

        elif choice == 2:
            shape_name = int(input("""Enter Shape:   1  |   2
            1)Sphere 
            2)Cube
            :               """))
            if shape_name == 1:
                x = factory.create_sphere()
            elif shape_name == 2:
                x = factory.create_cube()
            print(f"Volume: {x.volume():.3f}")
            print(f"Surface Area: {x.surface_area():.3f}")


client()