class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

obj = Person("Hridoy",25)
print(obj)