class RailwayForm:
    formtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}\nTrain name is {self.train}")
harrysapp = RailwayForm()
harrysapp.name = input("Enter your name:\n")
harrysapp.train = input("Enter your train's name:\n")
harrysapp.printData()