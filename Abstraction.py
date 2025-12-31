from abc import ABC, abstractclassmethod
class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10*5
    
r=Rectangle()
print(r.area()) 
    