#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.If the string length is less than 2,return instead of the empty string.
#Sample String : 'GLSUniversity'
#Expected Result : 'GLty'

str= input("Enter a sample string : ")
str1 = str[0:2]
strLen = len(str)
str2 = str[strLen-2:strLen+1]

print("Result is : ",str1+str2)
