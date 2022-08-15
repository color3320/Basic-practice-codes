#using list
num = int(input("Enter a number: "))
fib = [0, 1]
n1 = 0 
n2 = 1
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    fib.append(n3)
print("Fibonacci Series: ", fib)

#not using list
# num = int(input("Enter a number: "))
# n1 = 0
# n2 = 1 
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2,num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print (n3, end=" ")
# print()