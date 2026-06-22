class Student:
    college = 'CGC University'
    branch = 'AIML'
    course = "BTech"
    def _init_(self,stu_name,stu_rollno):
        self.name = stu_name
        self.rollno = stu_rollno
    def display_stu_info(self):
        print(self.name,self.rollno)
    # def ch_batch(self,new): #Modify
    #     print(self.ch_batch)


# 3 oject
s1 = Student('Manish',251002239)
s2 = Student('Rahul oggy',2510002267)
s3 = Student('Prince Raj',2510002230)
# print(s1.name)
# print(s1.rollno,"\n",s1.college,"\n",s1.branch,"\n",s1.course)
# print(s2.name)
# print(s2.rollno,"\n",s2.college,"\n",s2.branch,"\n",s2.course)
# print(s3.name) 
# print(s3.rollno,"\n",s3.college,"\n",s3.branch,"\n",s3.course) 

s1.display_stu_info()
s2.display_stu_info()
s3.display_stu_info()