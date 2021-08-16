import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices_images = [rock, paper, scissors]

user_choice=int(input("What do you want choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(user_choice >=3 or user_choice < 0):
    print("Invalid Input!! You Lose.")
    exit()
else:
    print("You chose:\n")
    print(choices_images[user_choice])

computer_choice=random.randint(0,2)
print("Computer chose:\n")
print(choices_images[computer_choice])

if((user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0)):
    print("You Lose!!")
elif(user_choice == computer_choice):
    print("It's a Draw!!")
else:
    print("You Win!!")