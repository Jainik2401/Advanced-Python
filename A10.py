#Write a Python program to create a calculator. Accept two nos from users and operation to perform. 
#According to the input given by the user calculate the result and display it.
print("calculator")

print("Choice")
print("1 for addition")
print("2 for substraction")
print("3 for multiphication")
print("4 for divison")
choice = int(input("Enter your choice : "))

n1 = float(input("Enter first number : "))
n2 = float(input("Enter second number : "))

if(choice == 1):
    print((f"addition of {n1} and {n2}  is "),n1+n2)
elif(choice == 2):
    print((f"substraction of {n1} and {n2}  is "),n1-n2)
elif(choice == 3):
    print((f"multiphication of {n1} and {n2}  is "),n1*n2)
elif(choice == 4):
    print((f"divison of {n1} and {n2}  is "),n1/n2)
else:
    print("Wrong choice")



