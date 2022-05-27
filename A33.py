#Write a Python program to create a dictionary with cricket players names and scores in a match. Retrieve runs entered by the players names.
cricket = {"sachin":98,"dhoni":100,"kohli":200}
playerName = input("Enter your player name : ")
if(playerName in cricket):
    print(f"run of {playerName} is {cricket[playerName]}")
else:
    print("player is not in dict")
