# no.1
'''
def maxi_num(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3       
m = int(input("Enter the 1st maximum number:\n"))
mm = int(input("Enter the 2nd maximum number:\n"))
mmm = int(input("Enter the 3rd maximum number:\n"))
n = maxi_num(m,mm,mmm)
print(f"The maximum number among {m},{mm} and {mmm} is {n}")
'''
# no 3
'''def conv_farh(cel):
    return (cel*(9/5)) + 32 
c = int(input("Enter the celsius :\n"))
print(f"The fahreneit temperature of {c} is {conv_farh(c)}")
'''
# no 4
'''print("Hello",end=", ")
print("How",end=" ")
print("are",end=" ")
print("you?",end=".")
'''
# no 5
'''
def sum_recursive(n):
    if n==1:
        return 1
    else:
        return sum_recursive(n-1) + n
n1 = int(input("Enter the no for addition:\n"))
f = sum_recursive(n1)
print(f"the sum first n number:{f}")
'''
# no 6
'''
n = int(input("Enter the no. of row:\n"))
for i in range(n):
    print("*" * (n-i))
'''
# no 7
'''
def conv_cm(inc):
    return inc*2.54
inc = int(input("Enter the inch :\n"))
print(f"The centimeter of {inc} is {conv_cm(inc)}")'''
# no 8
'''def rem_word(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()
newstr= input("Enter a sentences:\n")
remword = input("Enter the word to be remove:\n")
n = rem_word(newstr,remword)
print(f"the sentences is {newstr} and\nwanted to remove {remword} and\n the striped one:\n{n}")'''
# no 9
def multi_recursive(n,i):
    print(f"{n} X {i} = {n*i}")
    if(i<=10):
        multi_recursive(n,i+1)
num = int(input("Enter a number:\n"))
print(f"Multiplication table of{num} is:")
multi_recursive(num,1)
