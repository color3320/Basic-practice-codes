num = int(input("Enter a number to find factorial of: "))
fact = 1
if num<0:
    print("Not possible")
else:
    for i in range(1, num+1):
        fact = fact*i
print("Factorial of the given number is",fact)