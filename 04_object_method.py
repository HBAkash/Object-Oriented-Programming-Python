class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def myfnc(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")
obj = Person("Hridoy",25)
obj.myfnc()