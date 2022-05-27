#Write a Python program to sum all the items in a dictionary.
dict1 = {'a':100,'b':200,'c':300}
sum = 0
for data in dict1.values():
    sum = sum + data
print(f"sum of dictionary is {sum}")
