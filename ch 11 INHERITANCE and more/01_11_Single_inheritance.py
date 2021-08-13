class Empolyee:
    company = "Google"
    def showDtails(self):
        print("This is an empolyee")
class Programmer(Empolyee):
    language = "Python"
    def getLanguage(self):
        print(f"The language is {self.language}")
e = Empolyee()
e.showDtails()
p = Programmer()
p.showDtails()
print(p.company)