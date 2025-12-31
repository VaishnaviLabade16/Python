#Book Class
'''
class Book
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_details(self):
        print(f"Book name is {self.title} and Author name is {self.author}")

s1 = Book("Harry Potter", "J.K. Rowling")
s1.show_details()
'''
#inheritance
'''
class Vehicale:
    def start(self):
        print("Vehicale are collection of all vheicale")

class Bike(Vehicale):
    def start(self):
        print("Bike havbe 2 weels")
    
d=Bike()
d.start()
'''

#Abstraction
'''
from abc import ABC, abstractclassmethod
class Appliance(ABC):
    @abstractclassmethod
    def turn_on(self):
        return

class Fan(Appliance):
    def turn_on(self):
        print("Fan")
    
r=Fan()
print(r.turn_on()) 
'''

#Encapsulation
'''
class Mobile:
    def __init__(self, battery):
        self.__battery = battery  # private variable

    def charge(self, value):
        self.__battery = value

    def check_battery(self):
        return self.__battery


a = Mobile(100)
a.charge(50)
print(a.check_battery())
'''

#Task1
'''
class student:
   def __init__(self, name, age):
      self.name=name
      self.age=age

   def details(self):
      print(f"my name is {self.name} and age is {self.age}")

s = student("vaishu",20)
s.details()
'''

#Task2
'''
class Car:
   def __init__(self, brand, model):
      self.brand=brand
      self.model=model

   def details(self):
      print(f"my name is {self.brand} and age is {self.model}")

s1 = Car("Tata","Seeara")
s2 =Car("BMW","BMW")
s.details()
'''
#Task3
'''
class Book
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_details(self):
        print(f"Book name is {self.title} and Author name is {self.author}")

s1 = Book("Harry Potter", "J.K. Rowling")
s1.show_details()
'''

#Task 6
'''
class BankAccount:
    def __init__(self, balance):
       self._balance=balance #private variable
    
    def deposit(self,amount):
        self._balance+=amount

    def get_balance(self):
        return self._balance
    
account=BankAccount(1000)
account.deposit(500)
print(account.get_balance())
'''

#Task 7 create a class employee with private variable salary and name. 
# use getter and setter method to access them give me code in python
'''
class Employee:
    def __init__(self, name, salary):
        self.__name = name      # private variable
        self.__salary = salary  # private variable

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        self.__salary = salary


# Creating object
e1 = Employee("Rahul", 30000)

# Accessing using getters
print(e1.get_name())
print(e1.get_salary())

# Modifying using setters
e1.set_name("Amit")
e1.set_salary(40000)

print(e1.get_name())
print(e1.get_salary())
'''

# Task 8 Create an abstract class shape with an abstract method draw().
#  Create a subclass Circle that implements the method
'''
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Subclass
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

# Creating object of Circle
c = Circle()
c.draw()
'''

#Task 9 Create an abstract class vheicle() with an abstract method start().
#Create a class Bike that overrides the method

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# Child class
class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

# Creating object
b = Bike()
b.start()
