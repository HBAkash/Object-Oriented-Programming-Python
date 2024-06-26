'''
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
'''


class Person:
    def __init__(funny,name,age):
        funny.name = name
        funny.age = age
    def __str__(aemon):
        return f"My name is {aemon.name} Targaryan and I am {aemon.age} years old"
obj = Person("Daemon",35)
print(obj)