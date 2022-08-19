n1 = int(input("Enter a number: "))
conv2str1 = str(n1)
sqn1 = n1**2
conv2str2 = str(sqn1)
if conv2str2.endswith(conv2str1):
    print("Automorphic")
else:
    print("Not automorphic")
