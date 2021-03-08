# n=int(input("Enter an integer: "))
# d = dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)

class Student():
    def __init__(self, name):
        self.name=name
        self.age=0
        self.math_mark=0

    def setAge(self, age):
        self.age=age

    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Math mark:',self.math_mark)

    def setMarks(self, mark):
        self.math_mark=mark

s=Student('Son')
s.setAge(22)
s.setMarks(10)
s.display()