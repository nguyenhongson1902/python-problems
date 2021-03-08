# result = []
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         result.append(str(i))
# print(','.join(result))
import math


class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return self.radius*self.radius*math.pi

    def getCircumference(self):
        return self.radius*2*math.pi

c=Circle(5)
print(c.getArea())
print(c.getCircumference())