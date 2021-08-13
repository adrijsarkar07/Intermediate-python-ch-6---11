# no 1
'''num1 =int(input("Enter number 1:\t"))
num2 =int(input("Enter number 2:\t"))
num3 =int(input("Enter number 3:\t"))
num4 =int(input("Enter number 4:\t"))
if(num1>num4):
    f1 = num1
else:
    f1 = num4
if(num2>num3):
    f2 = num2
else:
    f2 = num3
if(f1>f2):
    print(str(f1) +" is the greatest than f2")
else:
    print(str(f2) + " is the greatest than f1")'''
# no 2
'''
marks1 = int(input("Enter your marks out of 100:\t"))
marks2 = int(input("Enter your marks out of 100:\t"))
marks3 = int(input("Enter your marks out of 100:\t"))
marks4 = int(input("Enter your marks out of 100:\t"))
marks_percent = (marks1+marks2+marks3)/300*100
if(marks_percent>40):
    print("congratulation! you have passed the exam")
elif(marks_percent==33):    
    print("congratulation! you have passed the exam")
else:
    print("ohh..! you failed in exam. Better luck next time!")'''
# no 3.
'''text1 = input("Enter text\n")
if("make a lot of money" in text1):
    spam = True
elif("buy now" in text1):
    spam = True
elif("subscribe this" in text1):
    spam = True
elif("click this" in text1):
    spam = True
else:
    spam = False
if(spam):
    print("This text is spam")
else:
    print("This text isn't spam")
'''
# n0 4,
'''name = input("Enter your name\n")
if(len(name)>=10):
    print(" your name contains characters  more than or equal to 10 ")
else:
    print("your name contains characters less than 10")'''
# n0 5.
'''name = input("Enter the name\t")
namelist = ["Adrij","Atri","Durba","Anup"]
if name in namelist:
    print("your name is presnt in the list  : "+ name)
else:
    print("Not found!")
'''
# no 6
'''marks1 = int(input("Enter your marks out of 100:\t"))
marks2 = int(input("Enter your marks out of 100:\t"))
marks3 = int(input("Enter your marks out of 100:\t"))
marks4 = int(input("Enter your marks out of 100:\t"))
mark = (marks1+marks2+marks3+marks4)/4
if (mark>=90):
    print("your marks is ",mark,"you got grade : EX")
elif(mark>=80):
    print("your marks is ",mark,"you got grade : A")
elif(mark>=70):
    print("your marks is ",mark,"you got grade : B")
elif(mark>=60):
    print("your marks is ",mark,"you got grade : C")
elif(mark>=50):
    print("your marks is ",mark,"you got grade : D")
elif(mark<50):
    print("your marks is ",mark,"you got grade : F")'''
# no 7
post = input("Enter a post: ")
if ("HARRY" in post):
    print("Yes! the post contains the name Harry.")
elif ("harry" in post):
    print("Yes! the post contains the name Harry.")
elif ("HaRry" in post):
    print("Yes! the post contains the name Harry.")
elif ("hArRy" in post):
    print("Yes! the post contains the name Harry.")
elif ("haRRy" in post):
    print("Yes! the post contains the name Harry.")
elif ("harrY" in post):
    print("Yes! the post contains the name Harry.")
else: 
    print("No! the post does not contain the name Harry")