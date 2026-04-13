imort Time
#Generators
'''
--> This is a special type of function that return an ITTERATION which one at a time

#yield:
--> it will take a pause and again resume , this is not a nrml keyword cannot be used in normal functions
--> This is used to produce a value and pause execution.

#next():
--> This is used to get the next value from the generator
--> When the value is finished , it will stop the iterator
'''
'''
def myGenerator():
    yield 1
    yield 2
    yield 3
i=myGenerator() # yeild value id stored int variable to priont it
print(next(i))
print(next(i))
print(next(i))


def square(n):
    for i in range(n):
        yield i*i     # catches the value and sends to main code
for val in square(5):# yeild value must be stored in the variable to use it or print it
    print(val)
'''

def numbers(n):
    for i in range(n+1):
        yield i
n=numbers(100)
for i in n:
 print(i)
 time.sleep(2)
