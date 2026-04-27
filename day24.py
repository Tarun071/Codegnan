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

import re 
any="this is a method can used to read entire file and this can be done"
we="hello"
so=re.findall("[a-z]",any)
an=re.search("[a]",any)
the=re.findall("h...o",we)
the2=re.search("h...o",we)
print(the)
print(the2)