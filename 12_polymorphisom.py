class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print(f"Drive {self.brand} {self.model} and relax! ")
class Boat():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print(f"Float {self.brand} {self.model} and Chill! ")

class Plane():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print(f"Fly {self.brand} {self.model} and enjoy! ")

car1 = Car("Audi", "Q8")
boat1 = Boat("Ibiza","Touring20")
plane1 = Plane("Boeing","747")

for x in (car1,boat1,plane1):
    x.move()