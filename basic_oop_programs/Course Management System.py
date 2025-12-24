class Student:
    def _init_ (self,name, grade):
        self.name = name 
        self.grade = grade
class Course :
    def __init__ (self, subject, capacity):
        self.subject = subject
        self.capacity = capacity
        self.students = []
    def add_students (self,student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        else:
            return False
    def get_average_grade (self):
        sum = 0
        for student in self.students:
            sum += student.grade
        avg = sum/len(self.students)
        return avg
    def  get_topper (self):
        topper = self.students[0]
        for student in self.students:
            if student.grade > topper.grade:
                topper =  student
            return topper
s1 = Student("Sevita",85)
s2 = Student("Urvashi",90)
s3 = Student("Rahul",78)
course = Course("Mathematics",2)
print(course.add_students(s1))
print(course.add_students(s3))
print(course.add_students(s2))
print(course.get_average_grade())
print(course.get_topper().name)
