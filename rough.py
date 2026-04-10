'''a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a,"is greatest number")
elif b>a and b>c:
    print(b,"is greatest number")
elif c>a and c>b:
    print(c,"is greatest number")

w=input()
count=1
for i in w:
    if i==" ":
        count+=1
print(count)'''


#list of even numbers
def check():
    
    l=[]
    for i in a:
        if i%2==0:
            l.append(i)
    if len(l)==0:
        print("No even numbers ")
    else:
        print(" even numbers are : ",l)


a=[1,3,5] 
