#no 1
'''
m = int(input("Enter number:\t"))
for i in range(11):
    print(m,"*",i,"=",m*i)
'''
#no 2
'''
l1 = ["Harry","Shubam","Sachin","Rahul"]
for name in l1:
    if name.startswith("S"):
        print("Good morning",name)
    else:
        pass
'''
# no 3
'''
m = int(input("Enter number:\t"))
i = 0
while i<=10:
    print(m,"X",i,"=",m*i)
    i +=1
'''
# no 4
'''
m = int(input("Enter number:\t"))
prime = True
for i in range(2,m):
    if(m%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number isn't Prime")
'''
#no 5.
'''
num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)
'''
#no 6.
'''
n = int(input("Enter number:\t"))
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print(f"The factorial of {n} is {factorial}")
'''
#no 8
'''
n = int(input("Enter the no. of rows:\t"))
for i in range(n):
    print("* " *(i+1))
'''
#no 7.
'''
n = int(input("Enter the no. of rows:\t"))
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))
'''
#no 9

s = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern") 
for i in range(s):
    for j in range(s):
        if(i == 0 or i == (s - 1) or j == 0 or j == (s - 1)):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()


