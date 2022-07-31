# traditional method
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp>0:
    rem = temp%10
    # print(digit)
    sum = sum + rem**3
    temp = temp//10
if num == sum:
    print(num, "is a Armstrong number")
else:
    print(num,"is not an Armstrong number")
