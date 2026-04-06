#function
'''
--> Function is a block of code whhich is reusable
--> Two types: 1.Buil-in or in-build
               2.user defined

'''
'''
def add(a,b): #--- the a,b are parameters
    print(a+b)

def isEvenOrNot(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
def pali(s):
    rev=""
    #return str[::-1]==str
    for i in s:
        rev=i+rev
    return s==rev
        

a=int(input())
b=int(input())
add(a,b)#--- this a,b are arguments


print(pali("hoh"))
'''

#is operator
a=[10,20]
b=[20,10]
b=a
print(a is b)
