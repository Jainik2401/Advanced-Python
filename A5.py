#Write a Python program to get unique values from a list.
list = [1,2,2,3,4,3,4,10]
count = 0
for i in list:
    count = list.count(i)
    if(count == 1):
        print("Unique value is : ",i)