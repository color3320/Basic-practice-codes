# traditional method
num1 = int(input("Enter a starting number: "))
num2 = int(input("Enter a ending number: "))

for i in range(num1,num2+1):
    sum = 0
    temp = i
    while temp>0:
        rem = temp%10
        # print(digit)
        sum = sum + rem**3
        temp = temp//10
    if i == sum:
        print(i)
    #    For numbers to be in line
        # print(i,end=" ")