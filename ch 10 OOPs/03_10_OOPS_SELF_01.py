class Empolyee:
    company = "Google"
    def getSalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
harry = Empolyee()
harry.salary = 1100000
harry.getSalary()