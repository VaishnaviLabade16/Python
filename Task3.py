#INHERITANCE
#Person --> Student
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll


s = Student("Amit", 20, 101)
print(s.name, s.age, s.roll)
'''

#Animal --> Dog
'''
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def  bark(self):
        print("Dog barks")

d=Dog()
d.eat()
d.bark() 
'''

#Vehicle --> Car
'''
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, fuel):
        super().__init__(speed)
        self.fuel = fuel

c = Car(120, "Petrol")
print(c.speed,c.fuel)
'''

#Account --> Saving_Account
'''
class Account:
    def __init__(self, balance):
        self.balance = balance

class SavingAccount(Account):
    def interest(self):
        return self.balance*0.05
    
a = SavingAccount(10000)
print(a.interest())
'''     

#Person->Employee->Manger
'''
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id


class Manager(Employee):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept


m = Manager("Raj", 201, "HR")
print(m.name, m.emp_id, m.dept)
'''
#MULTIPLE INHERITANCE
#Device --> Mobile --> Smartphone
'''
class Device:
    def power(self):
        print("Power ON")

class Mobile(Device):
    def call(self):
        print("Calling")

class Smartphone(Mobile):
    def internet(self):
        print("internet access")

s=Smartphone()
s.power()
s.call()
s.internet()
'''

#Shape --> Rectangele --> Cuboid
'''
class Shape:
    pass


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


class Cuboid(Rectangle):
    def __init__(self, l, w, h):
        super().__init__(l, w)
        self.h = h

    def volume(self):
        return self.l * self.w * self.h
c = Cuboid(10, 5, 3)
print("Area of Rectangle:", c.area())
print("Volume of Cuboid:", c.volume())
'''
#Company --> Department --> Employee
'''
class Company:
    def company_name(self):
        print("ABC Ltd")


class Department(Company):
    def dept_name(self):
        print("IT")


class Employee(Department):
    def emp_name(self):
        print("Suresh")


e = Employee()
e.company_name()
e.dept_name()
e.emp_name()
'''

#HERARCHICAL INHERITANCE
#Animal → Dog, Cat
#Each child has its own sound() method.
'''
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Dog barks"

class Cat(Animal):
    def sound(self):
        return "Cat meows"

# Example
dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())
'''

#Employee → Developer, Tester
#Each calculates salary differently.
'''
class Employee:
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        base = 50000
        bonus = 10000
        return base + bonus

class Tester(Employee):
    def calculate_salary(self):
        base = 40000
        incentive = 5000
        return base + incentive

# Example
dev = Developer()
tester = Tester()
print(dev.calculate_salary())
print(tester.calculate_salary())
'''

#Shape → Circle, Square
#Each computes its own area.
'''
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Example
circle = Circle(5)
square = Square(4)
print(circle.area())
print(square.area())
'''

#Vehicle → Bike, Truck
#Each has different mileage logic.
'''
class Vehicle:
    def mileage(self):
        pass

class Bike(Vehicle):
    def mileage(self):
        return "Bike mileage: 60 km/l"

class Truck(Vehicle):
    def mileage(self):
        return "Truck mileage: 8 km/l"

# Example
bike = Bike()
truck = Truck()
print(bike.mileage())
print(truck.mileage())
'''

#MULTIPAL INHERITANCE
#Task 13: Father + Mother → Child
'''
# Parent classes
class Father:
    def skills(self):
        return "Gardening"

class Mother:
    def skills(self):
        return "Cooking"

# Child inherits from both Father and Mother
class Child(Father, Mother):
    def all_skills(self):
        return f"{Father.skills(self)}, {Mother.skills(self)}"

# Example usage
child = Child()
print("Child skills:", child.all_skills())
'''

#Task 14: Camera + Phone → SmartDevice
'''
# Parent classes
class Camera:
    def take_photo(self):
        return "Photo taken!"

class Phone:
    def make_call(self, number):
        return f"Calling {number}..."

# Child inherits from Camera and Phone
class SmartDevice(Camera, Phone):
    pass

# Example usage
device = SmartDevice()
print(device.take_photo())
print(device.make_call("123-456-7890"))
'''

#Task 15: Engine + Wheels → Car
'''
# Parent classes
class Engine:
    def start_engine(self):
        return "Engine started!"

class Wheels:
    def drive(self):
        return "Car is moving!"

# Child class
class Car(Engine, Wheels):
    pass

# Example usage
my_car = Car()
print(my_car.start_engine())
print(my_car.drive())
'''

#Task 16: Writer + Editor → Author
'''
# Parent classes
class Writer:
    def write(self):
        return "Writing a story..."

class Editor:
    def edit(self):
        return "Editing the draft..."

# Child class
class Author(Writer, Editor):
    pass

# Example usage
author = Author()
print(author.write())
print(author.edit())
'''

#Hybrid Inheritance
#Task 17: Person → Employee → Manager / Intern
#(Combination of hierarchical + multilevel)
'''
# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Person: {self.name}"

# Employee inherits from Person
class Employee(Person):
    def work(self):
        return f"{self.name} is working"

# Manager inherits from Employee
class Manager(Employee):
    def role(self):
        return f"{self.name} manages the team"

# Intern inherits from Employee
class Intern(Employee):
    def role(self):
        return f"{self.name} is an intern"

# Example usage
manager = Manager("Alice")
intern = Intern("Bob")
print(manager.info(), "-", manager.role())
print(intern.info(), "-", intern.role())
'''

#Task 18: Animal → Mammal → Dog / Bat
#(Demonstrating hybrid structure)
'''
# Base class
class Animal:
    def breathe(self):
        return "Breathing..."

# Mammal inherits Animal
class Mammal(Animal):
    def feed_milk(self):
        return "Feeding milk"

# Dog inherits Mammal
class Dog(Mammal):
    def sound(self):
        return "Woof!"

# Bat inherits Mammal
class Bat(Mammal):
    def sound(self):
        return "Screech!"

# Example usage
dog = Dog()
bat = Bat()
print(dog.breathe(), dog.feed_milk(), dog.sound())
print(bat.breathe(), bat.feed_milk(), bat.sound())
'''

#Task 19: Account → SavingsAccount / CurrentAccount / BusinessAccount
'''
# Base class
class Account:
    def __init__(self, balance):
        self.balance = balance

    def info(self):
        return f"Balance: ${self.balance}"

# SavingsAccount inherits Account
class SavingsAccount(Account):
    def interest(self):
        return f"Interest added: ${self.balance * 0.05}"

# CurrentAccount inherits Account
class CurrentAccount(Account):
    def overdraft(self):
        return "Overdraft available"

# BusinessAccount inherits Account
class BusinessAccount(Account):
    def loan(self):
        return "Business loan approved"

# Example usage
s = SavingsAccount(1000)
c = CurrentAccount(500)
b = BusinessAccount(2000)

print(s.info(), "-", s.interest())
print(c.info(), "-", c.overdraft())
print(b.info(), "-", b.loan())
'''

#Task 20: School → Teacher → SubjectTeacher / Student
#(Combination of hierarchical + multilevel)
'''
# Base class
class School:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"School: {self.name}"

# Teacher inherits School
class Teacher(School):
    def teach(self):
        return "Teaching students"

# SubjectTeacher inherits Teacher
class SubjectTeacher(Teacher):
    def subject(self):
        return "Teaching Math"

# Student inherits School
class Student(School):
    def study(self):
        return "Studying subjects"

# Example usage
teacher = SubjectTeacher("Greenwood High")
student = Student("Greenwood High")

print(teacher.info(), "-", teacher.teach(), "-", teacher.subject())
print(student.info(), "-", student.study())
'''