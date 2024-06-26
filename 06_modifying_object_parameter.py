class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = 45

    def __str__(self):
        return f"My name is {self.name} age : {self.age}"

obj = Person("Hridoy", 25) #even if the argument is 25 but inside the class it goes upto 45
print(obj)