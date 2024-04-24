class Rectangle:
    def __init__(self,l,w):
        self.lenght = l
        self.width = w

    def rec_area(self):
        return self.lenght * self.width
    
    def rec_parameter(self):
        return 2 * self.lenght + 2 * self.width
    
try:
    x = int(input("Insert length of the rectangle: "))
    y = int(input("Insert width of the rectangle: "))
    
    if not type(x and y) is int:
        raise TypeError
    
    ThisRectangle = Rectangle(x,y)

    print(f"This is area of the rectangle {ThisRectangle.rec_area()} and parameter {ThisRectangle.rec_parameter()}")
except:
    print("Error")