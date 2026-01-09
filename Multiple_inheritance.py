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
