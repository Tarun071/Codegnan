'''def fac(n):
    if n ==0 or n==1:
        return 1
    else:
       return n*fac(n-1)
n=int(input())
print(fac(n))  
'''
#ATM system 

#Withdraw
def withdraw(amt,bal):
    if bal>amt:
        bal=bal-amt
        print("Money withdraw Succesfull")
       
    else:
        return "Insufficient funds"
#Deposit
def deposit(amt,bal):
    if amt%100==0 and amt>=5000:
        bal+=amt
    else:
        print("Amount should be more than 5000")
    print("Money Deposit succesful")

    
#Starter  
def ATM():
    pin={
        "pas":"0099"
        }
    p=input()
    if p==pin["pas"]:
        
        print("OPTIONS: 1.Withdraw 2.Deposit")
        n=int(input("ENTER YOU OPTION : "))
        b=1000
        if n==1:
            w=int(input("Enter money to withdraw : "))
            withdraw(w,b)
        elif n==2:
            d=int(input("Enter money to Deposit : "))
            deposit(d,b)
        elif n==3:
            print("Balance = ",b)
            
        else:
            print("Invalid Option")
    else:
        print("Wrong Pin")
    ATM()
#main   
ATM()


    
