class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        self.num2 = num2
        print(f"Lets add!")
        return self.num + num2.num
    def __mul__(self,num2):
        self.num2 = num2
        print(f"Lets mutliply!")
        return self.num * num2.num
n = int(input("Enter the number:\n"))
nn = int(input("Enter the number:\n"))
n1 = Number(n)
n2 = Number(nn)
c = n1 + n2
cc = n1 * n2
print(c)
print(cc)