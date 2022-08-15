from cmath import sqrt
import math
# num1 = math.floor(6.88)
# num2 = math.ceil(6.28)
# print(num1,num2)
n1 = int(input("Enter a number: "))
if math.floor(math.sqrt(n1)) == math.ceil(math.sqrt(n1)):
    print("Given number is a perfect square")
else:
    print("Given number is not a perfect square")