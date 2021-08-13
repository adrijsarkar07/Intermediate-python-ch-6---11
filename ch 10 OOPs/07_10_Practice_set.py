# no 1
'''class Programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the programmer is {self.name} and He is working in {self.product}")
harry = Programmer("Harry","Skype")
sarry = Programmer("arry","Azure")
larry = Programmer("Larry","X-box")
adrij = Programmer("Adrij","Github")
adrij.getInfo()
larry.getInfo()
sarry.getInfo()
harry.getInfo()'''
# no 2
'''class Calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"Square of {self.number} = {self.number **2}")

    def squareroot(self):
        print(f"Squareroot of {self.number} = {self.number **0.5}")

    def cube(self):
        print(f"Cube of {self.number} = {self.number **3}")
n = int(input("The number for sqrt , sq and cube:\n"))
a  = Calculator(n)

a.square()
a.squareroot()
a.cube()'''
# no 3
'''class sample:
    a = "Harry"
obj = sample()
obj.a = "Vikky"
print(sample.a)
print(obj.a)'''
#  no 4
'''class Calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"Square of {self.number} = {self.number **2}")

    def squareroot(self):
        print(f"Squareroot of {self.number} = {self.number **0.5}")

    def cube(self):
        print(f"Cube of {self.number} = {self.number **3}")
    @staticmethod
    def greet():
        print(f"******Hello here, welcome to the best calculator of the world ********")
n = int(input("The number for sqrt , sq and cube:\n"))
a  = Calculator(n)
a.greet()
a.square()
a.squareroot()
a.cube()'''
# no 5
'''class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in this train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is :Rs.{self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"your ticket has been booked and your seat no. is {self.seats}")
            self.seats -=1
        else:
            print("Sorry this train is full kindly try in tatkal")
    
intercity = Train("Intercity Express",200,2)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()'''
# no 6
class sample:
    def __init__(self,name):
        self.name = name
obj = sample("Harry")
print(obj.name)