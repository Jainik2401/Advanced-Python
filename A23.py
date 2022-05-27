#Write a Python program to find the elements in a given set that are not in another set.
set1 = (1,2)
set2 = (1,2,3,4)

lenOfset1 = len(set1)
count = 0
for i in set1:
    if(i in set2):
        count = count + 1
if(lenOfset1 == count):
    print(set1 , " is in ",set2)
else:
    print("not in set")
