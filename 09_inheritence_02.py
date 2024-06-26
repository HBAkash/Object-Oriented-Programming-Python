class parent():
    def __init__(self,fname,mname):
        self.father = fname
        self.mother = mname
    def printing(self):
        print(f"Father's name: {self.father} \n Mother's name: {self.mother}")

class lawclass(parent):
    def __init__(self, fname,mname,name, age):
        super().__init__(fname, mname)
        self.name = name
        self.age = age
    def prints(self):
        print(f"{self.name} {self.age}")


x = lawclass("Father in law name", "Mother in law name","Child name",35)
print(x.printing())



