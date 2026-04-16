#TASK

#1
'''
import pyttsx3
engine = pyttsx3.init()

def task_speaking_test(text):
    engine.say(text)
    engine.runAndWait()

task_speaking_test("Hello, My dear buddy ")

'''


#2
'''
import pyttsx3
audio = pyttsx3.init()

def task_speaking_test(text):
    audio.say(text)

name = "Dimple"
branch = "ECE"
college = " Miracle educational society group of institutions "
skills = "Python, C, Basics of VLSI"
goal = "I want to become a Software Engineer"
 

task_speaking_test("Hello, My dear buddy ")
task_speaking_test("My name is " + name)
task_speaking_test("i am final year " + branch )
task_speaking_test(" from " + college )
task_speaking_test("i am good at " + skills)
task_speaking_test("and  " + goal)

audio.runAndWait()
'''

#3


import pyttsx3
audio = pyttsx3.init()

def task_speaking_test(text):
    audio.say(text)


user_text=input("Enter your message: ").lower()

name="user"

if "my name is " in user_text:
    name=user_text.split("my name is")[-1].strip()
elif "name is " in user_text:
    name=user_text.split("name is")[-1].strip()

if user_text in["hi", "hello","hey"]:
    response="hello{name},how can i help you ?"
elif "name" in user_text:
    response=f"hello {name}, how can i help you ?"
else:
    response="sorry, i didn't understand ."

print(response)
task_speaking_test(response)
audio.runAndWait()