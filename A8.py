#Write a Python program to check weather given number is armstrong or not.
print("Armstrong number")
no = input("Enter your number : ")
noArray=[]
total = 0
for i in no:
    noArray.append(i)

arrLen = len(noArray)

mul = 1
total=0
for i in noArray:
    iInt = int(i)
    for j in range(0,arrLen):
       mul = mul*iInt
    total = total+mul
    mul=1

if(int(no)==total):
    print(f"{no} is Armstrong")
else:
    print(f"{no} isn't Armstrong")
