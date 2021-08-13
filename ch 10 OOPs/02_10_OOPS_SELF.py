class Empolyee:
    company = "Google"
    def getSalary(self):
        s1 = int(input("Enter the amount of salary:\n"))
        print(f"{n}'s salary is {s1} and he is working in {c}.")
# harry = Empolyee()
n = input("Enter your name:\n")
c = input("Enter your company's name:\n")
Empolyee.getSalary(n)