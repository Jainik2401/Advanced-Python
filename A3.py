#Write a Python program to remove duplicates from a list.

listvalue = [10,50,65,59,65,10,50]
print("List with duplicate ",listvalue)
setValue = set(listvalue)
listValue = list(setValue)
print("List without duplicate : ",listValue)