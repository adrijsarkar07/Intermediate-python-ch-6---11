# def factorial_iter(n):
#     product = 1
#     for i in range (n):
#         product = product * (i+1)
#     return product
# p = int(input("Enter the no. for factorial:\n"))
# f = factorial_iter(5)
# print(f)
def factorial_recursive(n):
    if n==0 or n==1:
        return 1

    return n *factorial_recursive(n-1)
n = int(input("Enter the no for factorial:\n"))
f = factorial_recursive(n)
print(f)
