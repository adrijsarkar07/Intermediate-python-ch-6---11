class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self,salary):
    #     self.__class__.salary = salary
    @classmethod
    def changeSalary(cls,salary):
        cls.salary = salary

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)