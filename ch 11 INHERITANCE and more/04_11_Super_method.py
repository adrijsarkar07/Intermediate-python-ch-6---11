class Person:
    country = "New Zealand"

    def __init__(self):
        print("Initializing person...\n")
  
    def takeBreath(self):
        print("I am breathing....")
class Empolyee(Person):
    company = "Youtube"
    def __init__(self):
        super().__init__()
        print("Initializing empolyee...\n")
    

    def getSalary(self):
        print(f"The salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so i am breathing.....")
class Programmer(Empolyee):
    company = "Facbook"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")
    

    def getSalary(self):
        print(f"no salary to Programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so i am breathing++...")
p = Person()
# p.takeBreath()

e = Empolyee()
# e.takeBreath()

pr = Programmer() 
# pr.takeBreath()