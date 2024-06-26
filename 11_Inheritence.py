class Person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(f"{self.fname} {self.lname}")

class Child(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year = year

    def disp(self):
        print(f"Hi! welcome {self.fname} {self.lname} to the class of {self.year}")

obj = Child("Hridoy","Banik",2024)
obj.disp()