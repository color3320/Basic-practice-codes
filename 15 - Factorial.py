def printDivisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i,end=" ")
        i = i + 1
         
n= int(input("Enter a number: "))
print ("The factors of",n, "are: ")
printDivisors(n)