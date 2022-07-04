#Inheritence in Python
class Person:
    def __init__(self,fname,lname) -> None:
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

x=Person("Sourav","Paul")
x.printname()