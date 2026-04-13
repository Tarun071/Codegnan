#ATM system 

#Withdraw
def withdraw(amt,bal):
    if bal>amt:
        bal=bal-amt
        print("Money withdraw Succesfull")
        return bal
       
    else:
        return "Insufficient funds"
#Deposit
def deposit(amt,bal):
    if amt:
        bal+=amt
        return bal
    else:
        print("Amount should be more than 5000")
    print("Money Deposit succesful")
    
    
#Starter  
def ATM():
    b=1000
    pin={
        "pas":"0099"
        }
    history=["4"]
    p=input("Enter your Pin :")
    print("***********************************************************************")
    while True:
        
        print("OPTIONS: \n1.Withdraw \n2.Deposit \n3.Check Balance \n4.History \n5.PIN change")
        n=int(input("\nENTER YOU OPTION : "))
        
        if n==1:
            w=int(input("Enter money to withdraw : "))
            b=withdraw(w,b)
            history.append(f"{w} DEBITED")
        elif n==2:
            d=int(input("Enter money to Deposit : "))
            b=deposit(d,b)
            history.append(f"{d} CREDITED")
        #check balance
        elif n==3:
            print("Balance = ",b)
        elif n==4:
            for i in history:
                print(i)
        elif n==5:
            oldPin=input("Enter your old PIN : ")
            if oldPin==pin["pas"]:
                newPin=input("Enter your old PIN : ")
                pin["pas"]=newPin
            else:
                print("PIN not matched")
            
        else:
            print("Invalid Option")
    else:
        print("Wrong Pin")
    print("*************************************************************************")
#main   
ATM()


    







