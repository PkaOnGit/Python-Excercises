class Time:
    def __init__(self,h,m,s):
        self.hour = h
        self.minute = m
        self.second = s

    def display(self):
        return(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
        
    def add(self,other):
        total_second = self.second + other.second
        total_minute = self.minute + other.minute + total_second//60
        total_hour = self.hour + other.hour + total_minute//60

        self.second = total_second % 60
        self.minute = total_minute % 60
        self.hour = total_hour % 24

try:

    x = int(input("Type in hour:"))
    y = int(input("Type in minute:"))        
    z = int(input("Type in second:"))
    i = int(input("Type in hour:"))
    j = int(input("Type in minute:"))        
    k = int(input("Type in second:"))

    if not type(z and y and x and i and j and k) is int:
        raise TypeError

    time1 = Time(x,y,z)
    time2 = Time(i,j,k)

    print(f"Time1 is {time1.display()}\nTime2 is {time2.display()}")

    print("This is sum of two time")

    time1.add(time2)
    print(time1.display())

except:
    print("Error")