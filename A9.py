#Write a Python program that will display all the palindrome numbers between 1 to 100
print("Palindrome number")
for i in range(1,101):
    noToStr = str(i)
    rev = noToStr[::-1]
    if(noToStr == rev):
        print(f"{i} is a palindrome number")