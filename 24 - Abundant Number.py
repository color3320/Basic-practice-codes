n = int(input("Enter a number: "))
sum = 0
for i in range(1,n):
    if n%i==0:
        #print(i)
        sum = sum+i
if sum>n:
    print("Abundant Number")
else:
    print("Not an Abundant Number")