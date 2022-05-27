#Write a Python program to check if a given key already exists in a dictionary
dict1 = {'a':100,'b':200,'c':300}
key = input("Enter your key : ")
if(key in dict1):
    print(f"{key} is available")
else:
    print(f"{key} is not available")
