'''
#Introduction to oops


OOP'S
-----
-->Object-Oriented Language (OOP) is a style of programming where we model real-world things as objects that contain both data and functions()
-->reusable  of code
--> and also scalable 

Class
-----
---->class is a blue-print or template that defines what kind of data and behaviour a certain type of object will have

Syntax-->class Class_Name:
            pass

object
------
-->Instance of class or an object is a real instance created from a class. it is the actual thing that exists in memory while the program run
car1=car()
car2=car()

Attributes
----------
--->these are variables that store data related to a class or object
'''
'''
class car:
    def  __init__(self,brand,color):
        self.brand = brand
        self.color = color
car1=car("BMW","White")
car2=car("Thar","Red")
print(car1.brand)
'''


class car:
    wheels=4
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=20
    def drive(self,miles):
        self.mileage+=miles
        return f"Drove  {miles} Miles. Total: {self.mileage}"
    def info(self):
        return f"{self.make} {self.model} {self.year}"
car1=car("BMW","Mustang","2008")
car2=car("Toyoto","Camry","2023")
print(car1.info())
print(car2.info())
print(car2.drive(10))