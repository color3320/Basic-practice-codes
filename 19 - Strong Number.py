num = int(input("Enter a number:"))
temp = num
sum = 0
while(num):
    i = 1
    fact = 1
    r = num%10
    while(i<=r):
        fact = fact*i
        i = i+1
    sum = sum+fact
    num = num//10
if(sum==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")