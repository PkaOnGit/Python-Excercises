import math

class circle:
    Pi = math.pi
    def __init__(self,r1,r2):
        
        self.radius1 = r1
        self.radius2 = r2

    def cir_area1(self):
        return circle.Pi * self.radius1 ** 2
    
    def cir_area2(self):
        return circle.Pi * self.radius2 ** 2
    
    def cir_circum1(self):
        return 2 * circle.Pi * self.radius1
    
    def cir_circum2(self):
        return 2 * circle.Pi * self.radius2

try:    
    x = int(input("This radius of circle1 : "))
    y = int(input("This radius of circle2 : "))

    if not type(x and y) is int:
        raise TypeError 
    
    
    bothcir = circle(x,y)

    print(f"These circle1 and circle2 informaion \nArea\nCircle1= {bothcir.cir_area1()}\nCircle2= {bothcir.cir_area2()}\nCircumference\nCircle1= {bothcir.cir_circum1()}\nCircle2= {bothcir.cir_circum2()}")

except:
    print("Error")
