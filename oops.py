print("Question 1")
class circle:
    def __init__(self):
        self.radius=10
    def getArea(self):
        self.area=3.14*(self.radius**2)
        print(self.area)
    def getcircumference(self):
        print(2*3.14*self.radius)
a=circle()
a.getArea()
a.getcircumference()

print("Question 2")

class student:
    def __init__(self):
        self.name=input("Enter Name")
        self.rollno=int(input("Enter Rollno"))
        self.age=0
        self.marks=0
    def display(self):
        print("Student Info")
        print(self.name,self.rollno,self.age,self.marks)
    def setAge(self):
        self.age=int(input("Enter Age"))
    def setmarks(self):
        self.marks=int(input("Enter Marks"))
x=student()
x.setAge()
x.setmarks()
x.display()


print("Question 3")

class temperature:
    def __init__(self):
        self.ctemp=0
        self.ftemp=0
    def convertFahrenheit(self):
        self.ctemp=float(input("Enter temperature in celsius"))
        self.ftemp=self.ctemp*1.8+32
        print(self.ctemp,"celsius=",self.ftemp,"Fahrenheit")
    def convertcelsius(self):
        self.ftemp=float(input("Enter temperature in celsius"))
        self.ctemp=(self.ftemp - 32) * 0.5556
        print(self.ftemp,"Fahrenheit=",self.ctemp,"celsius")
x=temperature()
x.convertFahrenheit()
x.convertcelsius()

print("Question 4")

class MovieDetails:
    def Display(self):
        print("Movie Details:")
        print("Artist Name:-",self.artist_name,"\nYear Of Release:-",self.year,"\nRating:-",self.rating)
    def Add(self):
        self.artist_name=input("Artist Name:- ")
        self.year=int(input("Year Of release:- "))
        self.rating=float(input("Rating"))
x=MovieDetails()
x.Add()
x.Display()
print("Question 5")

class animal:
    def info_(self):
        print("Class Animal")
class animal_attribute():
    def attribute(self):
        print("Class Animal_Attributes")
class tiger(animal,animal_attribute):
    def tiger_(self):
        print(" Class Tiger")
x=animal()
y=animal_attribute()
z=tiger()
z.info_()
z.attribute()

print("Question 6")
print("""OUTPUT:    A B
					A B"""


print("Question 7")
class shape:
    def methodarea(self):
        self.l=int(input("enter the length"))
        self.b=int(input("enter the breadth"))
class rectangle(shape):
    def methodarea(self):
        self.l=int(input("enter the length of rectangle"))
        self.b=int(input("enter The breadth of rectangle"))
class square(shape):
    def methodarea(self):
        self.l=int(input("enter the length of sides of square"))
x=shape()
y=rectangle()
z=square()
y.methodarea()
z.methodarea()
