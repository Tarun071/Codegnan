'''
k=n
sum=1
for i in range(1,n):
    if (n%i==0):
        sum=sum*i
if sum==k:
    print("perfect square")
else:
    print("not a perfetct square")

#sum of evens and odd in list
li=list(map(int,input().split()))
even=0
odd=0
for i in li:
    if i%2==0:
        even+=i
    else:
        odd+=i
print(even)
print(odd)'''


#table
'''
n=int(input())
for i in range(1,11):
     print(n,"*",i,"=",n*i)
'''

#finding count upper and lower letters in string
'''
string1=input()
upper=0
lower=0
for i in string1:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(upper)
print(lower)'''


'''
string1=input()
upper=[]
lower=[]
for i in string1:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
print(upper)
print(lower )
'''

#ATM machine validation
'''
ICIC_Raghu_AC_details={"Name":"Raghu","ATM PIN": "9100"}
print("Welcome to ICIC ATM")
print("Pls insert your ATM card")
ICIC_user_pin=input("Pls enter 4 digits ATM pin:")
if len(ICIC_user_pin)==4:
    if ICIC_user_pin in ICIC_Raghu_AC_details["ATM PIN"]:
        print("The pin is correct")
    else:
        print("You have entered invalid pin")
else:
    print("Plz enter 4 digit pin")



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
'''