class Empolyee:
    company = "Google"
    
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Empolyee is created !") 
    def getDetails(self):
        print(f"The name of the eempolyee is {self.name}\nhe is working in {self.subunit}\nsalary is {self.salary}")
    def getSalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("the time is 9AM in the morning")
harry = Empolyee("Harry",100000,"Youtube")
harry.getDetails()