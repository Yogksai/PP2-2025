#Parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Yerassyl", "Kadyrzhan")
x.printname() 

#Child Class
class Student(Person):
  def __init__(self,fname, lname):
     Person.__init__(self, fname, lname) 
x = Student("Mike", "Olsen")
x.printname()

#super()
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) 

#Properties
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Yerassyl", "Kadyrzhan", 2028)

#Methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
x = Student("Yerassyl", "Kadyrzhan", 2028)
x.welcome()