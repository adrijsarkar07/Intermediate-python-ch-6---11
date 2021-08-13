class Person:
    country = "New Zealand"
    def takeBreath(self):
        print("I am breathing....")
class Empolyee(Person):
    company = "Youtube"

    def getSalary(self):
        print(f"The salary is {self.salary}")
    def takrBreath(self):
        print("I am an Employee so i am breathing.....")
class Programmer(Empolyee):
    company = "Facbook"

    def getSalary(self):
        print(f"no salary to Programmers")
p = Person()
p.takeBreath()
e = Empolyee()
e.takeBreath()
pr = Programmer() 
pr.takeBreath()