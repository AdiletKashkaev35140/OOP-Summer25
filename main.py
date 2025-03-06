class Person_Adilet:
    x = 5

print(Person_Adilet)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Adilet", 20)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Adilet", 20)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Adilet", 20)
p1.myfunc()