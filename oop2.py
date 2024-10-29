# create a class called Person, that has 3 attributes(name,age,gender)
# the create constructor method and method and object

class Person:
    # constructor method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def onyesha(self):
        print(f"My name is {self.name} and my age is {self.age} and my gender is {self.gender}")

myobj=Person("Ivan", 20, "MALE")
myobj.onyesha()


class Trial:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print(f"My name is {self.name}, my age is {self.age}, my gender is {self.gender}")

obj = Trial("Kevin", 20, "MALE")
obj.show()