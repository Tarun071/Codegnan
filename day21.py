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


'''
#Single inheritence
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

'''
#Multiple inheritence
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





class Father:
    def show(self):
        print("This is Father class")

class Mother:
    def show1(self):
        print("This is Mother class")

class Child(Father, Mother):
    def display(self):
        print("This is Child class:")
        super().show1()

c = Child()
c.display()