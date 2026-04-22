'''
#Encapsulation
---------------
-->The principle of binding data (atrributes) and methods that operate on that data into a single unit, which is a class

'''


'''
class BankAC:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
Acc=BankAC(15000)
Acc.deposite(7000)
print(Acc.get_balance())
'''


'''
Inheritance
-----------
-->This allows a child class (subclass) to acquire the attributes and method of a parent class(Base Class) this is called Inheritance
1.Single Inheritance
--->A child class inherits from one parent class.
2.Mutiple
--->A child class inherits from more than one parent class



super()
-------
-->This is used to call methods of the parent class from the child class

'''

# ____________________________________________ 
'''
#Single inheritence
__________________________________________
class parent:
    def display(self):
        print("This is parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is child method")
obj=child()
obj.display()
'''
# ____________________________________________________
'''
#Multiple inheritence
__________________________________________________
class Father:
    def skill_1(self):
        print("Gymrat")
class mother:
    def skill_2(self):
        print("Cooking")
class child(Father,mother):
    def skill_3(self):
        print("Programming")
Obj=child()
Obj.skill_1()
Obj.skill_2()
Obj.skill_3()

        

'''

# class Father:
#     def show(self):
#         print("This is Father class")

# class Mother:
#     def show1(self):
#         print("This is Mother class")

# class Child(Father, Mother):
#     def display(self):
#         print("This is Child class:")
#         super().show1()

# c = Child()
# c.display()

# _______________________________________________________________________
#Multilevel inheritance
'''
--> This occurs whaen a class inherits 
'''
# _____________________________________________________________________
# class grandparent:
#     def showgp(self):
#         print("Iam grandParent")
# class parent(grandparent):
#     def showp(self):
#         print("Iam parent")
# class child(grandparent):
#     def showc(self):
#         print("Iam child")

# c1=child()
# c1.showp()

#___________________________________________________________________
#Hierarchy
#___________________________________________________________________
'''
class parent:
    def par(self):
        print("IAM PARENT")
class child1(parent):
    def c1(self):
        print("Print child 1")
class child2(parent):
    def c2(self):
        print("iam child 2")
class child3(child1,child2):
    def c3(self):
        print("Iam child 3")
ob=child3()
ob1=parent()
ob1.par()
ob.par()
_______________________________________________________________________________________________________________________________________
'''
# Polymorphism
'''
_________________________________________________________________________________________________________________________________________
--> Polymorphism means “many forms”.
--> In Object-Oriented Programming, polymorphism allows the same function/method name to behave differently depending on the object or data type.
--> Simply: One name, different behavior.

This allows a object of different classes to be treated as instance of the same base class , with methods behaving differently based on the actual object typeprint(
eg....
------
print(len("Python"))
print(len([1,2,3])
'''


'''
Method Overloading
------------------
-->This defines multiple methods with the same name but different parameters (number,type,or order) in the same class
'''

'''

class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
Cal=calculator()
print(Cal.add(2))
print(Cal.add(3,4))
print(Cal.add(5,7,8))
'''



'''
method Overriding
-----------------
--->This occurs in the child class,redefining a parent class method with the same signature for runtime.


class animal:
    def speak(self):
        return "Sound"

class dog(animal):
    def speak(self):
        return "Woof"
DOG=dog()
print(DOG.speak())

class calculator:
    def sub(self,a,b=0,c=0):
        return a-b-c
c1=calculator()
print(c1.sub(1))
print(c1.sub(9,7))
print(c1.sub(9,8,7))

'''

#operator overloading
''' 
--> this is customized operator like +,- for user-defined classes by E.g-__add__,__sub__


class someone:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return someone(self.a +other.a,self.b+other.b)
    def __str__(self):
        return f"({self.a},{self.b})"
any=someone(2,3)
so=someone(5,9)
print(any+so)
'''

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
c=circle(5)
print(c.area())