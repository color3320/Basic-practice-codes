# Traditional method/linear quest to find HCF
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
hcf = 1

for i in range (1,min(n1,n2)+1):  #using min function because if n1 is 36 and n2 is 60, 
    if n1%i == 0 and n2%i == 0: #hcf will not be greater than 36 so the range of i will become 1 to 36
        print(i)
        hcf = i
print("HCF = ",hcf)

#Euclidean Algorithm - Repeated Subtraction 
# n1 = int(input("Enter number 1: "))
# n2 = int(input("Enter number 2: "))
# while n1 != n2:
#     if n1>n2:
#         n1 = n1 - n2
#     else:
#         n2 = n2 - n1
# print("HCF = ",n1)