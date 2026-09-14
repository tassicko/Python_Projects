class person():
    def speak(self):
        print("person speaks")


class student(person):
    def speak(self):
        print("boy speaks") 



obj = student()
obj1 = person()
obj.speak()
obj1.speak()