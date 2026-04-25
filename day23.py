#File handling
'''
--> File handler is an object od file to maintain several functions of file such as creating , reading, writing and update also deleting the file

How to open a file
------------------
1.open()
-->this open fuction takes two parameters and in this we have to close the file by calling close() function after program
   1.file name
   2.mode
2.with open()
    modes("r","w","a","x","t")
-------------------------------------------------
1. "r" -- Read
    -->To read the file we use this mode and if the file does'nt exist it will throw the error 

2. "w" -- write
    -->to write the text into the file
3. "a" -- append
    --> to add the text into the file this is used and it will create the file if it doesn't exist
---------------------------------------------------------------------------------------------------
To read a file :
read () -- Use the .read() method to pull the entire content into a single string. This is best for smaller files.
readlines() -- the readlines() method is used to read all lines from a file and return them as a list of strings, where each element in the list represents a single line including its trailing newline character (\n).
'''

#r
any=open("demo.txt","r")
print(any.read())
any.close()

#w
any=open("demo.txt","w")
any.write("vanakkam!")
any.close()

#a
