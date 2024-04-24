class Distance:
    def __init__(self,f,i):
        self.feet = f
        self.inch = i

    def add(self,other):
        total_inch = self.toinch() + other.toinch()

        new_inch = total_inch % 12
        new_feet = total_inch // 12
        return Distance(new_feet,new_inch)

    def toinch(self):
        return self.feet * 12 + self.inch

    def compare(self,other):
        if self.toinch() > other.toinch():
            return ("Fisrt distance is longer")
        elif self.toinch() == other.toinch():
            return ("Both distance are equal")
        else: 
            return ("Second distance is longer")

try:

    x = int(input("Insert first feet distance: "))
    y = int(input("Insert first inch distance: "))
    i = int(input("Insert second feet distance "))
    j = int(input("Insert second inch distance "))

    if not type(x and y and i and j) is int:
            raise TypeError

    distance1 = Distance(x,y)
    distance2 = Distance(i,j)

    sum_distance = distance1.add(distance2)

    print(distance1.compare(distance2))
    print(f"The sum of both distance is {sum_distance.feet} feet and {sum_distance.inch} inch")

except:
    print("Error")