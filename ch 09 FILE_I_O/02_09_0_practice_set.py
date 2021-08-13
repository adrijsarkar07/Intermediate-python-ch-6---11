# no 1
'''f = open('poems.txt')
t = f.read()
if 'Twinkle' in t:
    print("Twinkle is presnt in the file")
else:
    print("Twinkle is not present in the file")
f.close()'''
# no 2
'''n = int(input("Enter the highscore:\n"))
def game():
    return n
score = game()

with open("highscore.txt") as f:
    highscore = f.read()
if highscore=='':
    with open("highscore.txt",'w') as f:
        f.write(str(score))
elif int(highscore)<score:
    with open("highscore.txt",'w') as f:
        f.write(str(score))'''
# no 3
'''for i in range(2,21):
    with open(f"Tables(2-20)/Mutliplication_tables_of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
            if j!=10:
                f.write('\n')'''
# no. 4
'''with open("sample.txt") as f:
    content = f.read()
content = content.replace("Donkey","@#$!&**&^!$#!%!&*")

with open("sample.txt",'w') as f:
    f.write(content)
'''
# no 5
'''m1,m2,m3,m4=input("Enter the 1st words:\n"),input("Enter the 2nd words:\n"),input("Enter the 3rd words:\n"),input("Enter the 4th words:\n")
words=[m1,m2,m3,m4]
with open("sample.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"@#$!&**&^!$#!%!&*")
    with open("sample.txt",'w') as f:
        f.write(content)'''
# no 6
'''
with open("samplelog.txt") as f:
    content = f.read()
if 'python' in content.lower():
    print("Yes!,python is in this log file....") 
else:
    print("no!,python isn't in this log file....")'''
# no 7
'''content = True
i = 1
with open("samplelog.txt") as f:
    while content:
        content = f.readline()
        
        if 'python' in content.lower(): 
            print(content)
            print(f"Yes!,python is in this log file on line no. {i}")
        i+=1'''
# no 8
'''with open("this.txt")as f:
    content = f.read()    

with open("copy.txt",'w') as f:
    f.write(content)'''
# no 9
'''file1 = "this.txt"
file2 = "copy.txt"
with open(file1) as f:
    f1 = f.read()
with open(file2) as f:
    f2 = f.read()
if f1 == f2:
    print("The files are identical to each other")
else:
    print("The files aren't identical")'''
# no 10
'''with open("this.txt") as f:
    f.write("")'''
# no 11
import os
oldn = "a.txt"
newm ="renamed_by_python.txt"
with open(oldn)as f:
    content = f.read()
with open(newm,'w') as f:
    f.write(content)
os.remove(oldn)