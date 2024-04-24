class Box1:
    def __init__(self,w,h,d):
        self.width1 = w
        self.height1 = h
        self.depth1 = d
    
    def volume1(self):
        return self.height1 * self.width1 * self.depth1
    
    def sur_area1(self):
        return self.height1 * self.width1 * 2 + self.width1 * self.depth1 * 2 + self.height1 * self.depth1 * 2
class Box2:
    def __init__(self,w,h,d):
        self.width2 = w
        self.height2 = h
        self.depth2 = d
    
    def volume2(self):
        return self.height2 * self.width2 * self.depth2
    
    def sur_area2(self):
        return self.height2 * self.width2 * 2 + self.width2 * self.depth2 * 2 + self.height2 * self.depth2 * 2
    
try:
    a = int(input("Width of the first box: "))
    b = int(input("Height of the first box: "))
    c = int(input("Depth of the first box: "))

    i = int(input("Width of the second box: "))
    j = int(input("Height of the second box: "))
    k = int(input("Depth of the second box: "))

    if not type(a and b and c and i and j and k) is int:
        raise TypeError
        
    First = Box1(a,b,c)
    Second = Box2(i,j,k)

    print(f"Volume of boxes\nBox1= {First.volume1()}\nBox2= {Second.volume2()}")
    print(f"Surface area of boxes\nBox1= {First.sur_area1()}\nBox2= {Second.sur_area2()}")

except:
    print("Error")