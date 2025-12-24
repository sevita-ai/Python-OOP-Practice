class Student:
    def __init__ (self,name):
        self.name = name
        self.marks = []
    def add_mark (self,mark):
        if 0 <= mark <= 100:
            self.marks.append(mark)
            return True
        else:
            return False
    def get_average (self):
            if len(self.marks) == 0:
                return 0
            sum = 0
            for i in self.marks:
                sum +=i
            avg = sum/len(self.marks)
            return avg
s1 = Student("Sevita")

print(s1.add_mark(85))   
print(s1.add_mark(90))   
print(s1.add_mark(110)) #Invalid
print(s1.add_mark(45))

print("Average:", s1.get_average())
