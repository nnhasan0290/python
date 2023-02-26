class MyClass: 
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print("full name is " + self.fname + " " + self.lname);


class Student(MyClass):
    def printName(self):
        super().printName()
        print("from student " + self.fname + " " + self.lname)

x = Student("fname", "lname")
x.printName()