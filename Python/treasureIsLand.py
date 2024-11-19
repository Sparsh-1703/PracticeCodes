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
/______/______/______/______/______/______/______/______/______/______/_____/
********************************************************************************''')
print("Welcome to the Treasure Island! ;)")
print("Your mission is to find the Treasure.")
choice1= input('You\'re at a crossroad, where do you want to go? "Left or Right?" ').upper() #use backslash for escaping the string/program recognition.

if choice1 in ["LEFT", "L"]:
    choice2 = input('''You\'ve come to a Lake, there\'s an Island in the middle of the lake. 
                    Type "wait" to wait for a Boat. Type "swim" to swim across. ''').upper()
    if choice2 == "SWIM":
        choice3 = input('''You arrived at the Island unharmed. 
                        There's a house with 3 doors, 1 Red, 1 Blue, 1 Yellow, 
                        which color would you choose? ''').upper()
        if choice3 == "BLUE":
            print("HOORAY! You found the Treasure.")
        elif choice3 == "YELLOW":
            print("It's a room full of fire. Game Over! ")
        elif choice3 == "RED":
            print("You entered a room full of Beasts. You're never getting out! ")
        else:
            print("Invalid Answer! Respawn.")
    else:
        print("GAME OVER! You got attacked by an angry Trout.")
else:
    print("You fell into a hole. GAME OVER :(")