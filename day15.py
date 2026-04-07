'''a="Python is a programming language"
c=0
for i in a:
    if i==" ":
       c+=1
print(c+1)
'''


'''Ways to pass arguments in calling function
Required arguments
------------------
--> It should match same number variable in calling with def 

num=9
num_2=10
def add(num,num_2):
    print(num)
add(num,num_2)



--->Default argument
My_name="Raghu"
def add(My_name):
    print(My_name)
add(My_name="Dimple")
add(My_name="Avanthi")
'''

'''
#prime number
def isprime(n,count):
    for i in range(1,n):
        if n%i==0:
            count+=1
    if count==1:
        print("It is a Prime number")
    else:
        print("It is not a Prime number")
n=int(input())
count=0
isprime(n,count)
'''


def star(*kids):
    print(kids[2])
t=[1,2,4,4]
star(1,2,3,4,5)

























