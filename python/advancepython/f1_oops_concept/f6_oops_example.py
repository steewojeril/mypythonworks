class Course:
    def add_course_details(self, **kwargs):
        self.course_name = kwargs.get("course_name")
        self.status = kwargs.get("status")

    def __str__(self):  # String representation of the Course object
        return self.course_name


class Batch:
    def add_batch(self, **kwargs):
        self.course = kwargs.get("course")  # Each batch is linked to a course
        self.batch_code = kwargs.get("batch_code")
        self.start_date = kwargs.get("start_date")

    def __str__(self):  # String representation of the Batch object
        return self.batch_code


class Student:
    def add_student(self, **kwargs):
        self.student_name = kwargs.get("student_name")
        self.email = kwargs.get("email")
        self.batch = kwargs.get("batch")  # Each student is linked to a batch

    def __str__(self):  # String representation of the Student object
        return self.student_name


# Creating course instances
django = Course()
django.add_course_details(course_name="Django", status=True)
ms = Course()
ms.add_course_details(course_name="Mean Stack", status=True)
bd = Course()
bd.add_course_details(course_name="Big Data", status=True)

# Creating batch instances and linking courses to them
djb1 = Batch()
djb1.add_batch(course=django, batch_code="DJMay2K22B1", start_date="12-06-2022")
djb2 = Batch()
djb2.add_batch(course=django, batch_code="DJMay2K22B2", start_date="11-06-2022")

msb1 = Batch()
msb1.add_batch(course=ms, batch_code="MSMay2K22B1", start_date="12-06-2022")
msb2 = Batch()
msb2.add_batch(course=ms, batch_code="MSMay2K22B2", start_date="12-06-2022")

# Creating student instances and linking batches to them
steewo = Student()
steewo.add_student(student_name="Steewo", email="steewojeril@gmail.com", batch=djb1)
siva = Student()
siva.add_student(student_name="Siva", email="siva@gmail.com", batch=djb2)
tinu = Student()
tinu.add_student(student_name="Tinu", email="tinu@gmail.com", batch=msb1)
deego = Student()
deego.add_student(student_name="Deego", email="deego@gmail.com", batch=msb2)

# Store all students in a list
students = [steewo, siva, tinu, deego]

# Find students enrolled in the 'Mean Stack' course
ms_students = [stud.student_name for stud in students if stud.batch.course.course_name == "Mean Stack"]
print(ms_students)  # Output: List of student names enrolled in the Mean Stack course
