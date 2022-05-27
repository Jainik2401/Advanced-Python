#Write a Python program to remove a specified item using the index from an array.
from array import *;
arr = array("i",[1,2,3,4,5,1,7])
arr2 = array("i",[])
print(arr)
index = int(input("Enter Index :"))
if(index < len(arr)):
    for i in range(0,len(arr)):
        if(i==index):
            continue
        else:
            arr2.append(arr[i])
    arr = arr2
    print(arr)
else:
    print("Invalid")
