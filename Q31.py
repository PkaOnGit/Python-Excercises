class Student:
    def __init__(self, n, r, m):
        self.name = n
        self.roll = r
        self.mark = m

    def total(self):
        return sum(self.mark)
    
    def percentage(self):
        total_mark = self.total()
        return (total_mark / len(self.mark))
    
    def division(self):
        percent = self.percentage()
        if percent >= 80:
            return "1st division"
        elif percent >= 60:
            return "2nd division"
        elif percent >= 45:
            return "3rd division"  
        else: 
            return "Fail"

try:
    students = []

    for i in range(1, 6):
        x = input(f"Enter name of student {i}: ")
        y = input(f"Enter roll number of student {i}: ")
        z = [int(mark) for mark in input(f"Enter 5 subjects marks for student {i} separated by spaces: ").split()]

        if not all(isinstance(mark, int) for mark in z):
            raise TypeError("Marks must be integers.")

        if not all(isinstance(x,str)):
            raise TypeError("Marks must be integers.")

        if not all(0 <= mark <= 100 for mark in z):
            raise ValueError("Marks must be between 0 and 100.")

        if len(z) != 5:
            raise ValueError("Exactly 5 subject marks must be entered.")

        students.append(Student(x, y, z))

    for student in students:
        print(f"Name: {student.name}")
        print(f"Roll Number: {student.roll}")
        print(f"Total Marks: {student.total()}")
        print(f"Percentage: {student.percentage():.2f}%")
        print(f"Division: {student.division()}")
        print()

except:
    print("Error")