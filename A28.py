#Write a Python program to convert a list to a tuple.28.Write a Python program to concatenate following dictionaries to create a new one.
#Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60
dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}

for key in dict2:
    dict1[key] = dict2[key]

for key in dict3:
    dict1[key] = dict3[key]
    
print(dict1)
