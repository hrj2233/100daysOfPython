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
choice1 = input('You\'re at a cross road. where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
        'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. "
            "One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "yellow":
            choice4 = input(
                'There are two treasure boxes there. '
                'One is a big box and the other is a small box. '
                'The door is closing suddenly. You have to choose quickly and go out. '
                'Which would you choose between the two? Type "big" or "small"\n')
            if choice4 == "small":
                choice5 = input(
                    'Now you can take this treasure and get out of this island. '
                    'The boat is already gone when I go back the way I came. '
                    'Are you going to make a raft and go out or wait for another ship to show up and save you? '
                    'Type "make" or "wait"\n')
                if choice5 == "make":
                    print("You succeeded and became rich.")
                else:
                    print("The natives showed up and took the treasure. Game Over.")
            else:
                print("You were stuck there and couldn't get out. Game Over.")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole. Game Over.")
