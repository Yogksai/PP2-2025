class MyClass:
    x = 5
    name = "Era"

p1 = MyClass()
print(p1.name) 
#__init__ function 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John",36)
print(p1.name, p1.age)

#__str function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Yarik", 17)
print(p1)

#Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
        print("Hello "+ self.name)
p1 = Person("Yarik", 17)
p1.myFunc()

#Self parametr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(abc):
        print("Hello "+ abc.name)
p1 = Person("Yarik", 17)
p1.myFunc()
#modify, delete
p1.age = 40
del p1.age
