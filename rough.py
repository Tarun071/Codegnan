# # '''a=int(input())
# # b=int(input())
# # c=int(input())
# # if a>b and a>c:
# #     print(a,"is greatest number")
# # elif b>a and b>c:
# #     print(b,"is greatest number")
# # elif c>a and c>b:
# #     print(c,"is greatest number")

# # w=input()
# # count=1
# # for i in w:
# #     if i==" ":
# #         count+=1
# # print(count)'''


# # #list of even numbers
# # def check():
    
# #     l=[]
# #     for i in a:
# #         if i%2==0:
# #             l.append(i)
# #     if len(l)==0:
# #         print("No even numbers ")
# #     else:
# #         print(" even numbers are : ",l)


# # a=[1,3,5] 


# def add(a,b):
#     print(a+b)
# def sub(c,d):
#     return c-d

# def mul(m,n):
#     m*n
# ####################################################
# a=8
# b=6

# add(a,b)
# k=sub(a,b)
# mul(a,b)
# print(k)


# if sub(a,b)>5:
#     print("true")
# else:
#     print("false")

#____________________________________________________________________________
#PYTHON CODES 
#Area of Rectangle
''' 
length=int(input())
width=int(input())
c=length*width
print("AREA OF RECTANGLE :", c )
'''
# user's name and age as input and prints a greeting message.
'''
name=input()
age=int(input())
print(f"Hello  {name} ! your {age} years old ")
'''
#check if a number is even or odd.
'''
num=int(input())
if num%2==0:
    print("Even number")
else:
    print("Odd number")
'''
#find the maximum and minimum values.
'''
a=list(map(int,input().split()))
maximum=max(a)
minimum=min(a)
print("Maximum number = ", maximum)
print("Minimum number = ", minimum)
'''
#check if a given string is a palindrome
'''
any=input()
if any==any[::-1]:
    print("palindrom")
else:
    print("not a palindrome")
'''
# Compound Interest Program
'''
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time Period (in years): "))

A = P * (1 + R/100) ** T
CI = A - P

print("Final Amount =", A)
print("Compound Interest =", CI)

'''
a=[1,2,-2,-3,1,-4]
s=0
for i in range(0,len(a)):
    if a[i]<0:
        a[i],a[s]=a[s],a[i]
        s+=1    
print(a)


#Convert number of days into years, weeks, and days
'''

days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365

weeks = remaining_days // 7
days_left = remaining_days % 7

print("Years:", years)
print("Weeks:", weeks)
print("Days:", days_left)
'''



#Find the sum of all positive numbers in a list
'''
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

sum_positive = 0

for num in numbers:
    if num > 0:
        sum_positive += num

print("Sum of positive numbers:", sum_positive)
'''

#Count number of words in a sentence
'''
sentence = input("Enter a sentence: ")

words = sentence.split()
count = len(words)

print("Number of words:", count)


#Swap the values of two variables

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
'''