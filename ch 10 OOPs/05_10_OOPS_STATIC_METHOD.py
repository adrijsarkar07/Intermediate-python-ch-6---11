class Empolyee:
    company = "Google"

    def getSalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("the time is 9AM in the morning")
harry = Empolyee()
harry.salary = 1100000
harry.greet()
harry.time()