num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
if num1 > num2 and num1>num3:
    print ("Number 1 is greater than number 2 and number 3 : ", num1)
elif num2 > num1 and num2>num3:
    print("Number 2 is greater than number 1 and number 3 : ", num2)
elif num3 > num1 and num3>num1:
    print("Number 3 is greater than number 1 and number 2 : ", num3)
else:
    print("All numbers are equal")