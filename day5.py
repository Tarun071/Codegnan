#string --> string is a collection of char
'''
STRING :
String is a datatype which stores sequence of characters in a variable. It is immutable (cannot be changed).

Types of methods or built-in functions used in string :

upper() – converts string into uppercase
lower() – converts string into lowercase
strip() – removes spaces from beginning and end
replace() – replaces a substring with another
split() – splits string into list
isdigit() – checks if all characters are digits
isalpha() – checks if all characters are alphabets
'''
'''

s = "  tarun talagana  "
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace("tarun", "rahul"))
words = s.split()
print(words)
print(result)
print(s.count("a"))
num = "1234"
print(num.isdigit())
name = "tarun"
print(name.isalpha())







# k=int(input())
any="Python programming language"
#any[7]="0"
# we cannot perform the modification because strin it not mutable
''' any="java"
print(any) 
#len()
num="123"
k=int(num)
print(k)
'''

time=input()
k=time.split(":")
print(k)

k[0]=int(k[0])-12
print(k[0],":",k[1])
    
