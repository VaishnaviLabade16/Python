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

