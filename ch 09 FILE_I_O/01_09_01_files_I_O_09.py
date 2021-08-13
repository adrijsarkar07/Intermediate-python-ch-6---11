'''# f = open("sample.txt",'r')
f = open("sample.txt")
# data = f.read()
data = f.read(5)
print(data)
f.close()'''
'''f = open("sample.txt")
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()'''
'''f = open('another.txt','w')
f.write("Please write this to the files.\nMy name is Adrij Sarkar.\nand I am a coder.")
f.close()'''
'''f = open('another.txt','a')
f.write("\nPlease write this to the files.\nMy name is Adrij Sarkar.\nand I am a coder.")
f.close()'''
with open('another.txt','w') as f:
    a = f.write("\nI am writing")
print(a)
# with open('another.txt','r') as f:
#     a = f.read()
# print(a)