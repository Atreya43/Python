class Person:
    def __init__(self,nm = "",gen = "",bdat = 11):
        self.name = nm;
        self.bdate = bdat;
        self.gender = gen;
    def set(self,nm = "",gen = "",bdat = 11):
        self.name = nm;
        self.bdate = bdat;
        self.gender = gen;
    def get(self):
        return (self.name,self.gen,self.bdate)
    def show(self):
        print("Name : ",self.name)
        print("Birth date : ",self.bdate)
        print("Gender : ",self.gender)

#

class Student(Person):
    def __init__(self,nm = "",gen="",bdat = 11,sem = 0,py_mark = 0,j_mark = 0,php_mark = 0):
        self.semester = sem;
        self.py_marks = py_mark;
        self.j_marks = j_marks;
        self.php_marks = php_mark;
        super.__init__(nm,gen,bdat)
    def set(self,nm = "",gen = "",bdat = 11,sem = 0,py_mark = 0,j_mark = 0,php_mark = 0):
        self.semester = sem;
        self.py_marks = py_mark;
        self.j_marks = j_mark;
        self.php_marks = php_mark;
        super().set(nm,gen,bdat)
    def get(self):
        super().get()
        return (sem,py_mark,j_mark,php_mark)
    def calc_total(self):
        Total = py_marks + j_marks + php_marks;
        return Total;
    def calc_per(self):
        Percentage = self.calc_total()//3
        return Percentage
    def calc_grade(self):

#
        


