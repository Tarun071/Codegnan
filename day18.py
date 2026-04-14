'''
Modules
-------
-->A module in a python is simply file that contain python code(Functions,Variable,classes)
-->To use modules, we have to use a keyword called import before the module
                                   Types of Modules
                                   ----------------
                            1.Built-in or Inbuilt     2.User-define modules

                            
'''

'''
#User defined modules
---------------------
-->This is developed by the user or programmer inside a file of python code and used by called import with filename...

Syntax--> import(keyword) file_name
           file_name.functionality

import mymodule
print(mymodule.add(4,7))
print(mymodule.sub(8,9))
'''


'''
Built-in or Inbuilt
-------------------
-->Already these are comes with installation and they are ready to use in the program
-->This is developed by the developer
Syntax-->import (keyword) module_name
         module_name.functionality
'''

'''
import math
print(math.sqrt(16))
'''


#small game using random module
import random as rd
count=1
k=rd.randint(1,10)
while count<4:
    guess=int(input(f"Guess the word (you have {4-count} chances) : "))
    if guess==k:
        print(f"You won the number is {k} ")
        break
    else:
        count+=1
if count==4:
 print("you lost out of chances ")
 ans=input("Do you what to know your number (yes/no) : ").lower()
 if ans=="yes":
     print(k)
        

    












