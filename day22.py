#exception handling
'''
--> try : tries the block of code and checkes wether it accepts or not
--> except :if try fails to execute and gives an error the except block will be excecutes 
-->finally: default block executes in default
'''
# try:
#     print(b)
# except:
#     print("erro occured")
# else:
#     print("hi rambabu")
# #___________________________________________________
# try:
#     b=1
#     print(b)
# except:
#     print("Error")
# else:
#     print("Code successfull")
# finally:
#     print("default message")
# #_____________________________________________________

# try:
#     b=[1,3,4,4]
#     print(b[23])
# except IndexError:
#     print("Error")

#
try:
    a=int(input())
    b=int(input())
    result=a/c
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("0 will not be divisible")
except NameError:
    print(f"Check the code")
else:
    print(f"result :{result}")
finally:
    print("This is end")
