class Student:
    college = 'CGC University'
    branch = 'AIML'
    course = "BTech"

    def __init__(self, stu_name, stu_rollno):
        self.name = stu_name
        self.rollno = stu_rollno

    def display_stu_info(self):
        print(self.name, self.rollno)


# 3 objects
s1 = Student('Manish', 251002239)
s2 = Student('Rahul Oggy', 2510002267)
s3 = Student('Prince Raj', 2510002230)

s1.display_stu_info()
s2.display_stu_info()
s3.display_stu_info()