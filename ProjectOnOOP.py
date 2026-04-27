class person:
    def __init__(self,person,edu):
        self.person=person
        self.edu=edu

class students:
    def __init__(self,person,edu,student_name,course):
        super().__init__(person,edu)
        self.student_name=student_name
        self.course=course
    def display(self):
        print(f"Student Name: {self.student_name}")
        print(f"eductaion: {self.edu}")
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
class professor(students):
    def __init__(self,person,pro_id,course):
        super().__init__(person)
        self.pro_id=pro_id
        self.course=course
    def display(self):
        print(f"Professor Name: {self.pro_name}")
        print(f"professor ID: {self.pro_id}")
        print(f"Course: {self.course}")

    # def course_details(self):
    #      print(f"Professor Name: {self.pro_name}")



obj1=students("98","B.TECH","tarun","pfs")
# obj2=professor(1,"Bhanu Teja","PFS")
obj1.display()
# # print("_________________________________\n")
# obj2.course_details()





















