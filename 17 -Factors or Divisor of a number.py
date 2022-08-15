num = int(input("Enter a number to find factors of: "))
i = 1
while i <= num:
    if (num%i == 0):
        print(i, end=" ")
    i = i + 1
print("are the factors of the number ",num)
