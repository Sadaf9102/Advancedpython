class Student:
    def getStudentdata(self, name, rollno):
        self.name=name
        self.rollno=rollno

class Test(Student):
    def getTestdata(self, math, sci):
        self.math=math
        self.sci=sci

class Sports(Student):
    def getSportsdata(self, sports):
        self.sports=sports

class result(Test, Sports):
    def __init__(self, name1, rno, m1,m2,m3):
        self.getStudentdata(name1, rno)
        self.getTestdata(m1,m2)
        self.getSportsdata(m3)

    def display(self):
        avg=((self.math+self.sci+self.sports)/150)*100
        print("name=",self.name)
        print("roll=",self.rollno)
        print("maths=", self.math)
        print("science=", self.sci)
        print("sports=", self.sports)
        print("average=", avg)

obj=result("Sadaf","20",42,41,38)
obj.display()
