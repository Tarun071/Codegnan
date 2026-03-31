#prime number
'''l=[1052,197,418,89]
p_count=0
for i in range(0,len(l)):
    count=0
    for j in range(2,l[i]+1):
        if l[i]%j==0:
            count+=1
    if count==1:
        p_count+=1
print(p_count)'''
#remove duplicates
'''
a=[2,345,6,5,2]
k=[]
for i in a:
    if i not in k:
        k.append(i)
print(k)'''

#armsrong number
n=153
c=n
sum=0
while(n!=0):
      r=n%10
      sum=sum+(r**3)
      n=n//10

if(c==sum):
    print("yes",sum)
else:
    print("no",sum)
