print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = str(input("You are at a crossroad. Where do you want to go? Select 'left' or 'right': ")).lower()
if choice1 == "left":
    choice2 = str(input("You arrived at a lake. There is an island in the middle of the lake. \nSelect 'Swim' to swim across or 'wait' to wait for a boat?: ").lower())
    if choice2 == "wait":
        choice3 = str(input("You arrive at a island with 3 doors. Select the 'red', 'yellow' or 'blue' door: ").lower())
        if choice3 == "red":
            print("You got burned by a fire. Game over!")
        elif choice3 == "yellow":
            print("You win!")
        elif choice3 == "blue":
            print("You got eaten by beasts. Game over!")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got attacked by a trout. Game over!")
else:
    print("You fell into a hole. Game over!")