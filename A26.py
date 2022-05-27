#Write a Python program to find the repeated items of a tuple.
tupleValue = (1,2,3,3,3,1)
listForCheck = []
count = 0
for value in tupleValue:
    if(tupleValue.count(value)>1):
        count = tupleValue.count(value)
        if(value in listForCheck):
            continue
        else:
            print(f"{value} is {count} reperat")
            listForCheck.append(value)
