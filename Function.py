#Right angled triangle

'''
num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
'''

#square triangle
'''
num=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end=" ")
    print()'''



#reverse a triangle
'''
num=int(input())
for i in range(num+1):
    for j in range(num-i):
        print("*",end=" ")
    print()
'''

#equalateral triangle
'''
num=int(input())
for i in range(num):
    for j in range(num-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
     print()

#alternate way
num=int(input())
for i in range(num):
    print(" "*(num-i),end="")
    for j in range(i+1):
        print("*",end=" ")
    print()    


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

#prime number
def isprime(n,count):
    for i in range(1,n):
        if n%i==0:
            count+=1
    if count==1:
        print(n,"It is a Prime number")
    else:
        print(n,"It is not a Prime number")
n=int(input()) 
count=0
isprime(n,count)
isprime(23,0)

def name(*raghu):
    print(raghu)
name(1,2,3)

#factorial
def fac(n):
    if n ==0 or n==1:
        return 1
    else:
       return n*fac(n-1)
n=int(input())
print(fac(n)) 

#perfect number
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")

    
def myGenerator():
    yield 1
    yield 2
    yield 3
i=myGenerator() # yeild value id stored int variable to priont it
print(next(i))
print(next(i))
print(next(i))


def square(n):
    for i in range(n):
        yield i*i     # catches the value and sends to main code
for val in square(5):# yeild value must be stored in the variable to use it or print it
    print(val)
'''