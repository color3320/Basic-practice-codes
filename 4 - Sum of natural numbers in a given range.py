num1 = int(input("Enter starting number: ")) 
num2 = int(input("Enter ending number: ")) 
sum = 0
for i in range(num1,num2+1):
  sum+=i
print(sum)