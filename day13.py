
#Right angled triangle

'''
num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
'''

#square triangle
'''
num=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end=" ")
    print()'''



#reverse a triangle
'''
num=int(input())
for i in range(num+1):
    for j in range(num-i):
        print("*",end=" ")
    print()
'''

#equalateral triangle
'''
num=int(input())
for i in range(num):
    for j in range(num-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
     print()
    '''

'''
#alternate way
num=int(input())
for i in range(num):
    print(" "*(num-i),end="")
    for j in range(i+1):
        print("*",end=" ")
    print()    
'''


ICIC_Raghu_AC_details={"Name":"Raghu","ATM PIN": "9100","Balance":5000}
print("Welcome to ICIC ATM")
print("Pls insert your ATM card")
ICIC_user_pin=input("Pls enter 4 digits ATM pin:")
if len(ICIC_user_pin)==4:
    if ICIC_user_pin in ICIC_Raghu_AC_details["ATM PIN"]:
        user_choice=int(input("Enter \n1.Withdraw: "))
        if user_choice==1:
            money_w=int(input("Enter money you want to withdraw"))
            if money_w<=ICIC_Raghu_AC_details["Balance"]:
                ICIC_Raghu_AC_details["Balance"] -= money_w
                print(ICIC_Raghu_AC_details["Balance"])
            else:
                print("insuff")
        else:
            print("Enter correct number")
    else:
        print("You have entered invalid pin")
else:
    print("Plz enter 4 digit pin")
    
