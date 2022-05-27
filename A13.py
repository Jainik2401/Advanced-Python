#Write a Python program to sort an element of the list using bubble sort.

list1 = [10,1,2,8,7]
print("bubble sort : ")
for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-i-1):
        if(list1[j] > list1[j+1]):
            temp = list1[j]
            list1[j] = list1[j+1] 
            list1[j+1] = temp
print("sorted list : ",list1)
 
