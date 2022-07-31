# traditional method

num = int(input("Enter a number: "))
sum = 0

while num!=0:
    rem = int(num%10)
    sum = sum + rem
    num = num/10
print(sum)

#string extraction
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)