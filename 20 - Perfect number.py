num = int(input("Enter a number: "))
sum = 0 
i = 1
for i in range(1, num):
    if num%i == 0:
        sum = sum + i
# print(sum)
if sum == num:
    print("Given number is a perfect number")
else:
    print("Given number is not a perfect number")