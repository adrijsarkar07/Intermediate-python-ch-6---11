class Number:
    def sum(self):
        return self.a + self.b
num = Number()
num.a = int(input("Enter the 1st number for addition:\n"))
num.b = int(input("Enter the 2nd number for addition:\n"))
s = num.sum()
print(f"{num.a} + {num.b} = {s}")