class Parent():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def prints(self):
        print(f"{self.fname} {self.lname}")

class Child(Parent):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduation = year
x = Child("Hridoy","Banik",2024)
print(x.graduation)