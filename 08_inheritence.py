#creating a parent class
class Person():
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)
x = Person("Hridoy","Banik")
x.printname()

#Overriding the parent class

class Student(Person):
    def __init__(self,fname,lname):
        self.first = fname
        self.last = lname
    def prints(self):
        print(f"{self.first} {self.last}")
y = Student("Akash", "Banik")
y.prints()