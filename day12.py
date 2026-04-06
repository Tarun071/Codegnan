#Control Statements
'''
Break--->this is used to exit from the loop, when we found the required value....

for j in range(1,10):
    print(j)
    if j==5:
        break

        
list_=[1,2,3,4]
for n in list_:
    print(n)
    if n==5:
        break'''


'''
#continue---> this is used to skip that particular loop
for j in range(1,10):
    if j == 5:
        continue
    print(j)


list_=[1,2,3,4]
for i in list_:
    if i==3:
        continue
    print(i)

'''

'''
#pass-->this is called as space holder
incase any statement like (if,for,else,elif...)this should complete,if not we will get syntax error to avoid this we are using pass

for j in range(1,100):
    pass
'''

'''
else -- for
-----------
it will fall back to else block, when all loops are completed 

for i in range(1,10):
    print(i)
else:
    print("else block")
'''

'''
while --- this a combination for and if statements, if we did not end the loop in proper way it wil run upto the memory space in the becomes empty
'''

#fibnacci series
'''
user_input=int(input())
a=0
b=1
c=0

for i in range(1,user_input+1):
    print(a,end=" ")
    c=a+b
    a,b=b,c
'''


#list operations
a=[3,2,1,3]
a.append(4)
a.extend([7,6])
a.sort()
a.count(3)
a.copy()
print(a)
    
