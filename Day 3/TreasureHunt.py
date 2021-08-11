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
step1 = input("Which direction would you like to go ? Left or Right \n")

if(step1.lower() == 'left'):
    step2 = input("You walked a mile and came across a river. Would you like to swim or wait for a boat? (swim or wait) \n")
    if(step2.lower() == 'swim'):
        print("Aaaaahhh!! Crocodile catched you while crossing the river!!\nGame Over!!")
    elif(step2.lower() == 'wait'):
        step3=input("Woooahhh!! You have successfully crossed the river and came across three doors among which you can only choose one. Which door would you like to choose 'Red' or 'Green' or 'Blue? \n")
        if(step3.lower() == 'red'):
            print("Oops!! The door you opened has room full of fire. \n Game Over!!")
        elif(step3.lower() == 'green'):
            print("Aaahh!! The door you open has Snakes all over the room. \n Game Over!!")
        elif(step3.lower() == 'blue'):
            print("Congratulations!! You opened the room which is full of jewels and treasure.")
        else:
            print("Wrong Choice!!")

elif(step1.lower() == 'right'):
    step2 = input("You came across a mountain Ditch. Would you like to trek or use a half broken bridge ? ( Trek or Bridge)\n")
    if(step2.lower() == 'trek'):
        print("Ooops!! You were eaten by Wild Animals.\nGame Over!!")
    elif(step2.lower() == 'bridge'):
        print("Aaaahhh!!! You fell off the Bridge.\n Game Over!!")


