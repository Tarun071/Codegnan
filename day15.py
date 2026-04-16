'''
a="Python is a programming language"
c=0
for i in a:
    if i==" ":
       c+=1
print(c+1)



Ways to pass arguments in calling function
Required arguments
------------------
--> It should match same number variable in calling with def 

num=9
num_2=10
def add(num,num_2):
    print(num)
add(num,num_2)



Default argument
----------------
-->It will take the default values from the arguments
My_name="Raghu"
def add(My_name):
    print(My_name)
add(My_name="Dimple")
add(My_name="Avanthi")
##############################################
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

####################################
def any(num,num_3,num_2):
    print(f"num = {num}, num_2={num_2}, num_3={num_3}")
any(num_2=7,num=0,num_3=90)

#Variable length Arguments:
---------------------------
--->Adding a star (*) before the parameter name in the function ,recieve a tuple of arguments and can access items with the indexes

def name(*raghu):
    print(raghu)
name(1,2,3)

#types of error
1.Syntax error
2.Indentation error
'''