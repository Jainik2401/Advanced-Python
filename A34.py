#Write a Python program to get the number of occurrences of a specified element in an array.
from array import *
arr = array("i",[1,2,3,1,3,3])
print(arr)
count = 0
for i in arr:
    if(arr.count(arr[i]) > 1):
        count = arr.count(arr[i])
        print(f"occurance of {arr[i]} is {count}")
        count = 0
    
