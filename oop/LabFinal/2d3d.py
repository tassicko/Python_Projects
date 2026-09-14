from abc import ABC, abstractmethod


class abstract_factory(ABC):                        # fix 1: inherit from ABC
    @abstractmethod
    def create_3d_shape(self, choice) -> 'shape3d':
        pass
    @abstractmethod
    def create_2d_shape(self, choice) -> 'shape2d': # fix 2: shape2d not shape3d
        pass


# ── 2D shapes ──────────────────────────────────────────
class shape2d(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class circle2d(shape2d):
    def __init__(self):                             # fix 4: added __init__
        self.r = float(input("give radius: "))
    def area(self):
        return 3.14 * self.r * self.r              # fix 3: actual logic
    def perimeter(self):
        return 2 * 3.14 * self.r                   # fix 3: actual logic

class square2d(shape2d):
    def __init__(self):                             # fix 4: added __init__
        self.a = float(input("give side: "))
    def area(self):
        return self.a * self.a                      # fix 3: actual logic
    def perimeter(self):
        return 4 * self.a                           # fix 3: actual logic

class shape_2d_factory(abstract_factory):
    def create_3d_shape(self, choice):
        pass
    def create_2d_shape(self, choice) -> 'shape2d':
        return circle2d() if choice == "circle" else square2d()


# ── 3D shapes ──────────────────────────────────────────
class shape3d(ABC):
    @abstractmethod
    def volume(self):
        pass
    @abstractmethod
    def surface_area(self):
        pass

class sphere3d(shape3d):
    def __init__(self):                             # fix 4: added __init__
        self.r = float(input("give radius: "))
    def volume(self):
        return (4/3) * 3.14 * self.r**3            # fix 3: actual logic
    def surface_area(self):
        return 4 * 3.14 * self.r**2                # fix 3: actual logic

class cube3d(shape3d):
    def __init__(self):                             # fix 4: added __init__
        self.a = float(input("give side: "))
    def volume(self):
        return self.a**3                            # fix 3: actual logic
    def surface_area(self):
        return 6 * self.a**2                        # fix 3: actual logic

class shape_3d_factory(abstract_factory):
    def create_2d_shape(self, choice):
        pass
    def create_3d_shape(self, choice) -> 'shape3d':
        return sphere3d() if choice == "sphere" else cube3d()


# ── main factory ───────────────────────────────────────
class factory():
    def create_factory(self, choice) -> "abstract_factory":
        return shape_2d_factory() if choice == "2dshape" else shape_3d_factory()


# ── usage ──────────────────────────────────────────────
f = factory()
choice = input("give choice (2dshape/3dshape): ")
fac = f.create_factory(choice)

if choice == "2dshape":
    name = input("give shape (circle/square): ")
    shape = fac.create_2d_shape(name)
    print(f"area: {shape.area()}")
    print(f"perimeter: {shape.perimeter()}")
else:
    name = input("give shape (sphere/cube): ")
    shape = fac.create_3d_shape(name)
    print(f"volume: {shape.volume()}")
    print(f"surface area: {shape.surface_area()}")