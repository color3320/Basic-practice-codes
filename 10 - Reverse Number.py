# traditional method
num = int(input("Enter a number: "))
temp = num
reverse = 0
while num>0:
    remainder = num%10
    reverse = (reverse*10) + remainder  
    num = num//10
# print(temp)
# print(reverse) 
if temp == reverse:
    print("Given number is a palindrome")
else:
    print("Given Number is not a palindrome")


#string slicing
num = int(input("Enter a number: "))
temp = str(num)[::-1]
rev = temp
rev = int(rev)
print(num)
print(rev)

if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
#print(rev)