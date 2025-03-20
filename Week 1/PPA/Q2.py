class Triangle:
    def __init__(self,a,b,c):
        self.s1 = a
        self.s2 = b
        self.s3 = c
    
    def Is_valid(self):
        if self.s1 + self.s2 > self.s3 and self.s1 + self.s3 > self.s2 and self.s3 + self.s2 > self.s1:
            return "Valid"
        return "Invalid"
    
    def Side_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
        elif self.s1 == self.s2 and self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"
    
    def Angle_Classification(self):
        lst = sorted([self.s1, self.s2, self.s3])
        if self.Is_valid() == "Invalid":
            return "Invalid"
        elif lst[0]**2 + lst[1]**2 == lst[2]**2:
            return "Right"
        elif lst[0]**2 + lst[1]**2 > lst[2]**2:
            return "Acute"
        else:
            return "Obtuse"
    
    def Area(self):
        s = (self.s1 + self.s2 + self.s3)/2
        area = (s*(s-self.s1)*(s-self.s2)*(s-self.s3))**(0.5)
        if self.Is_valid() == "Invalid":
            return "Invalid"
        else:
            return area
    
    
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())