class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin Cannot fly")

b=Bird()
p=Penguin()

b.fly()
p.fly()