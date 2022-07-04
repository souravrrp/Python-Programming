#function and class using python

class fullname:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def emp_name(self):
        print("My name is "+self.fname)

n=fullname("Sourav","Paul")
n.emp_name()