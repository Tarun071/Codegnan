#program to count vowels , consonants , spaces
'''
s="python is a programming language"
count=0
space=0
for i in s:
    if i!=" ":
        if i in "AEIOUaeiou":
            count+=1
    else:
        space=space+1
print("Vowels : ",count)
print("consonants : ",(len(s)-space)-count)
print("Spaces : ",space)
'''

# for loops
'''
a=9
print(a)
for i in range(1,10):
    print(i)
'''

#conversions
'''
any="123"
print(int(any))
print(list(any))
print(tuple(any))

so=123
print(str(so))

a=[(1,2),("w","e")]
print(dict(a))
'''

#some_programs
a="madam"
e=""
for i in a:
    e=i+e
if a==e:
    print("palindrome")
else:
    print("not palindrome")
