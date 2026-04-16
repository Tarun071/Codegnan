#check vowels or consonants
'''
letter=input()
if (letter.isalpha()):
    if letter in "AEIOUaeiou":
     print("IT's an vowel")
    else:
     print("its an consonant")
else:
    print("not an letter")

->print h from python

list=[1,2,3,"list",[1,2,["python","java"],"language"]]

print(list[4][2][0][3])
'''

'''
list : list is a datatype which stores set of elements in one variable, it is mutable.
types of methods or bulit in funcions used in list :
1- append() - adds element from the back of the list
2- extend() - it also adds into list but when it comes to add the another list it jus adds elements int the list not the whole list,even the strigs will be seapated as characters
3- remove()- uses element to delete ex: [23,23,45,32,90] l.remove(90).
4- pop()   - uses index to remove the element l.pop(0).
5- sort()
6-index()
7-clear()
8-insert()
9.reverse()
10-count()
11-len()


l=[1,2,3,"tarun",5]
l2=[7,8,9,10]
l.append(6)
print(l)

l.extend(l2)
print(l)

l.append(l2)
print(l)

name="tarun"
l.extend(name)
print(l)

l2.sort()
print(l2)

l.pop(0)
print(l)

l.index(2)
print(l)

l.reverse()





# print 100 prime numbers

def isPrime(n):
    count=0;
    for i in range(2,int(n**0.5)):
        if n%i==0:
             count+=1
    if count==0:
        return True
n=1
count=1
while(count<101):
    if isPrime(n)==True:
        print(n)
        count+=1
    n+=1    
    
            
'''



for i in range(0,5):
    for j in range(0,i):
        print(i)
    print()







