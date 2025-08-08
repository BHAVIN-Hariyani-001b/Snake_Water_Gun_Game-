# Snake drinks water → Snake wins
# Water douses gun → Water wins
# Gun kills snake → Gun wins

import random

youDict = {"s":1,"w":-1,"g":0}
options = {1: "Snake", -1: "Water", 0: "Gun"}

# com = random.randint(-1,1)

# rendom is choice to is require to list
com = random.choice(list(options.keys())) # it select random key

print("Snack - Water - Gun")
print("Select to [snack = s] , [water = w] , [gun = g]")

#player select your choich
youStr = input("Enter your choice : ").lower()
# check condition to player select choice is valid or not
if youStr not in youDict:
    print(f"Invalid Input {youStr} ,  Please enter 's', 'w', or 'g'.")
    exit()

you = youDict[youStr] 

#print to select item 
print(f"You are select is : {options[you]}")
print(f"Computer select is : {options[com]}")

if com == you:
    print("Its a draw")
elif (com == -1 and you == 1) or (com == 1 and you == 0) or (com == 0 and you == -1):
    print("You Win!")
else:
    print("You Loss!")

# OROROROROROO

# if com == you:
#     print("Its a draw")
# else:
#     if com == -1 and you == 1:
#         print("You Win")
#     elif com == -1 and you == 0:
#         print("You Loss")
#     elif com == 1 and you == -1:
#         print("You Loss")
#     elif com == 1 and you == 0:
#         print("You Win")
#     elif com == 0 and you == -1:
#         print("You Win")
#     elif com == 0 and you == 1: 
#         print("You Loss")
#     else:
#         print("Somting want wrong")

