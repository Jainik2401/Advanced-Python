#Write a Python program which will print Fibonacci series.
startNumber = int(input("Enter your number from where you want to start : "))
endNumber = int(input("Enter your number from where you want to finish : "))

n1 = startNumber
n2 = startNumber+1
print(n1)
print(n2)
for i in range(startNumber,endNumber+1):
    n3 = n1 + n2
    if(n3>endNumber):
        break
    print(n3)
    n1 = n2
    n2 = n3
