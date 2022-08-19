n1 = int(input("Enter a number: "))
sum = 0
temp = n1
while n1>0:
    sum = sum + n1%10
    n1 = n1//10
if(temp%sum==0):
    print("Harshad number")
else:
    print("Not Harshad number")
