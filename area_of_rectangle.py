# find area of the rectangle using self function:

class Rectangle():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def area (self):
        """Find area of the Rectangle"""
        return (self.x * self.y)

rec1 = Rectangle(x,y)
# print the result

print("Area is:",rec1.area())


    
