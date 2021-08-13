class Empolyee:
    company = "Google"
    salary = 100
harry = Empolyee()
rajni = Empolyee()
harry.salary = 300000
rajni.salary = 400000
print(harry.company)
print(rajni.company)
Empolyee.company = "Youtube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)