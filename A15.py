#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
sampleList = ['Red','Green','White','Black','Pink','Yellow']
print("sample list : ",sampleList)

arr = ["Red","Pink","Yellow"]
for i in arr:
    sampleList.remove(i)


print("Expected list : ",sampleList)
