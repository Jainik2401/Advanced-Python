#Write a Python program to check if a set is a subset of another set.
set1 = (1,2)
set2 = (1,2,3,4)

lenOfset1 = len(set1)
count = 0
for i in set1:
    if(i in set2):
        count = count + 1
if(lenOfset1 == count):
    print(set1 , " is a subset of ",set2)
else:
    print(set1 , " is not a subset of ",set2)
