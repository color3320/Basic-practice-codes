num1 = int(input("Enter starting number - "))
num2 = int(input("Enter starting number - "))

primenum= []

for i in range(num1,num2+1):
    flag = False

    if i<2:
        continue

    if i == 2:
        primenum.append(2)
        continue

    for x in range(2,i):          
        if (i % x) == 0:
            flag = True
            break

    if flag == False:
        primenum.append(i)
print(primenum)