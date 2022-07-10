class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")

    def __str__(self): #(this is called 'two string')(string representation)
        return self.course_name

class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course") #eth course nte batch aanu nnu kodukkan
        self.batch_code=kwargs.get("batch_code")
        self.start_date = kwargs.get("start_date")
    def __str__(self):
        return self.batch_code
class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email = kwargs.get("email")
        self.batch = kwargs.get("batch")
    def __str__(self):
        return self.student_name
django=Course()
django.add_course(course_name="django",status=True)
ms=Course()
ms.add_course(course_name="meanstack",status=True)
bd=Course()
bd.add_course(course_name="bigdata",status=True)

# print(django)

djb1=Batch()
djb1.add_batch(course=django,batch_code="djmay2k22b1",start_date="12-6-2022")
print(djb1.course) #to know the course of this batch
print(djb1.course.status) # and to know the status of that course  # nammal ingane connect cheyth kodutha karana aanu ingane edukkan pattunnath
# nammal ingane connect cheyth kodutha karana aanu ingane edukkan pattunnath

djb2=Batch()
djb2.add_batch(course=django,batch_code="djmay2k22b2",start_date="11-6-2022")

msb1=Batch()
msb1.add_batch(course=ms,batch_code="msmay2k22b1",start_date="12-6-2022")

msb2=Batch()
msb2.add_batch(course=ms,batch_code="msmay2k22b1",start_date="12-6-2022")

steewo=Student()
steewo.add_student(student_name="steewo",email="steewojeril@gmail.com",batch=djb1) #djb1 enna batch lottanu steewo add aayirikkunnath

siva=Student()
siva.add_student(student_name="siva",email="siva@gmail.com",batch=djb2) #djb2 enna batch lottanu siva add aayirikkunnath

tinu=Student()
tinu.add_student(student_name="tinu",email="tinu@gmail.com",batch=msb1) #msb1 enna batch lottanu tinu add aayirikkunnath

deego=Student()
deego.add_student(student_name="deego",email="deego@gmail.com",batch=msb2) #msb2 enna batch lottanu deego add aayirikkunnath

students=[]
students.append(steewo)
students.append(siva)
students.append(tinu)
students.append(deego)

# print students in meanstack

# for stud in students:
#     if stud.batch.course.course_name=="meanstack":
#         print(stud)
ms_studs=[stud.student_name for stud in students if stud.batch.course.course_name=="meanstack"]
print(ms_studs)