#Regular Expressions(RegEx)
'''
-->This regular expressionor RegEx is a sequense of characters that forms a searching pattern.
-->To use this we have to import re, which will unlock the package

FUNCTIONS:
----------
1.findall
--> by using this function it will find all the sequence of characters in the string
syntax-re.fundall(metachar,var_name")

2.search
--> by usung this function we can find the first sequence in the string
syntax--re.search("metachar",var_name)

META CHARACTERS:
----------------
--> metacharacter are used to form searching pattern
1.[]
-->In this metacharacter we can search for [a-z],[A-Z],[0-9]

import re 
any= "python is programming language"
so=re.findall("a",any)
print(so)

3.^
----
-> This is used to find the string is starting with the sequence 
syntax--> re.findall("metchar),var_name
'''

# import re 
# any="this is a method can used to read entire file and this can be done"
# we="hello"
# so=re.findall("[a-z]",any)
# an=re.search("[a]",any)
# the=re.findall("h...o",we)
# the2=re.search("h...o",we)
# print(the)
# print(the2)

# import re
# any="This meta character"
# an=re.findall("Th.?",any)
# print(an)

import re 
any="This is meta character will form"
an=re.findall("that|will",any)
print(an)


'''
#special sequence
-----------------
A special sequence is a \ followed by one of the characters in the list below,and has a

special meaning

\A
----
Returns a match if the specified characters are at the beginning of the string
Eg: "\AThe"
'''
# import re
# txt="The rain in Spain"
# #Check if the string starts with the "The":
# x=re.findall("\AThe",txt)
# print(x)
# if x:
#     print("Yes,there is a match!")
# else:
#     print("No Match")



'''
\b-Returns match where the specified characters are at the beginning or at the end of a word
Eg: r"\bain "

import re
txt="The rain in Spain"
#Check if the string starts with the "The":
x=re.findall("\bSpain",txt)
print(x)
if x:
    print("Yes,there is a match!")
else:
    print("No Match")


'''
