'''
ICIC_Raghu_AC_details={"Name":"Raghu","ATM PIN": "9100","Balance":5000}
print("Welcome to ICIC ATM")
print("Pls insert your ATM card")

ICIC_user_pin=input("Pls enter 4 digits ATM pin:")
if len(ICIC_user_pin)==4:
    
    if ICIC_user_pin in ICIC_Raghu_AC_details["ATM PIN"]:
        user_choice=int(input("Enter \n1.Withdraw:  \n2.Deposite: \n3.Pin change: \n4.Transcation History "))
        if user_choice==1:
            
            money_w=int(input("Enter money you want to withdraw"))
            if money_w<=ICIC_Raghu_AC_details["Balance"]:
                ICIC_Raghu_AC_details["Balance"] -= money_w
                print(ICIC_Raghu_AC_details["Balance"])
                
            else:
                print("insuff")
                
        elif user_choice==2:
            Deposite_m = int(input("plz enter the money you want to deposite: "))
            
            if Deposite_m % 100 == 0 and Deposite_m >=5000:
                ICIC_Raghu_AC_details["Balance"]+=Deposite_m
                
                print(f"you have depostied {Deposite_m} and the total ammount is {ICIC_Raghu_AC_details["Balance"]}")
            else:
                print(f"{Deposite_m} you have entered is change or less than given amount {5000}")
        elif user_choice ==3:
            old_pin=input("pls enter your old pin")

            if old_pin ==ICIC_Raghu_AC_details ["ATM PIN"]:
                new_pin=input("Enter new ATM PIN: ")
                
            if new_pin !=old_pin:
                ICIC_Raghu_AC_details ["ATM PIN"] = new_pin
                print("Your ATM pin updated succesfully")
                
            attempts_remaining==3
            while attempts_remaining > 0:
             old_pin = input("Enter your old ATM PIN: ")
             if len(old_pin)==4:
                if old_pin in user_choice["ATM PIN"]:
                   pin_change = input("Enter a new 4 digits ATM PIN: ")
                   user_choice["ATM PIN"]=pin_change
                   print("new pin is updated")
                
            else:
                print("you entered pin is incorrect")
            
        else:
            print("Enter correct number")
    else:
        print("You have entered invalid pin")
else:
    print("Plz enter 4 digit pin")



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


    







