class Student:
    def __init__ (self,name,rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
s1 = Student("Sevita",150)
s1.display()
