# class Employer:
#   def __init__(self, name, industry):
#     self.name = name          # attribute
#     self.industry = industry  # attribute

class Student:
  id = 24
  def __int__(self, name):
      self.name = name
  def __init__(self, id=78):
      self.id = id



s1 = Student(23)
s2 = Student('car')

s1.id = 23
print(s1.id, s2.id, sep=" ")

Student.id = 89
print( s1.id, s2.id, sep=" ")

