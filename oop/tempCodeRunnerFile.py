from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def square(self):
        pass
    @abstractmethod
    def mul(self):
        pass
class A(AbstractClass):
    def __init__(self, x):
        self.x = x

    def square(self):
        return self.x * self.x
    def mul(self):
        pass
class B(AbstractClass):
    def __init__(self, x):
        self.x = x
    def square(self):
        pass
    def mul(self):
        return self.x * 2

class Application:
    def call_method(self, choice):
        x = int(input("Enter value: "))
        if choice == "s":
            y = A(x)
            return y
        elif choice == "m":
            y = B(x)
            return y
            
def client():
    while True:
        c = int(input("quit?: "))
        if c == 3:
            break

        app = Application()
        choice = input("square or multiply: ")
        x = app.call_method(choice)
        if choice == "s":
            print(x.square())
        elif choice == "m":
            print(x.mul())
        
        print(type(x))             
        print(f"is instance of class A: {isinstance(x, A)}")        
        print(f"is instance of class B: {isinstance(x, B)}")           
        print(f"is instance of class AbstractClass: {isinstance(x, AbstractClass)}")

client()