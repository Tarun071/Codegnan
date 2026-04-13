#ATM system 

#Withdraw
def withdraw(amt,bal):
    if bal>amt:
        bal=bal-amt
        print("Money withdraw Succesfull")
       
    else:
        return "Insufficient funds"
#Deposit
def deposit(amt,bal,history):
    if amt%100==0 and amt>=5000:
        bal+=amt
    else:
        print("Amount should be more than 5000")
    print("Money Deposit succesful")
#History

    
    
#Starter  
def ATM():
    pin={
        "pas":"0099"
        }
    history=["4"]
    p="0099"
    while True:
        
        print("OPTIONS: 1.Withdraw 2.Deposit 3.Check Balance 4.History")
        n=int(input("ENTER YOU OPTION : "))
        b=1000
        if n==1:
            w=int(input("Enter money to withdraw : "))
            withdraw(w,b)
            history.append(w)
        elif n==2:
            d=int(input("Enter money to Deposit : "))
            deposit(d,b)
            history.append(d)
        #check balance
        elif n==3:
            print("Balance = ",b)
        elif n==4:
            for i in history:
                print(i)
            
        else:
            print("Invalid Option")
    else:
        print("Wrong Pin")
    
#main   
ATM()


    







