class Rectangle:
    def __init__ (self, length, breadth):
        self.length = length
        self.breadth = breadth
    def rec (self):
        area = self.length*self.breadth
        print("Area of rectangle with length ", self.length, "and breadth", self. breadth, "is: ", area)
        perimeter = 2*(self.length+self.breadth)
        print("Perimeter of rectangle with length ", self.length, "and breadth", self.breadth, "is: ", perimeter)
r1 = Rectangle(5,9)
r1.rec()
