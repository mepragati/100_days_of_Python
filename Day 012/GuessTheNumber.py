from art import logo
from random import randint

print(logo)
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5

number = randint(1,100)
while(lives > 0):
    print(f"You have {lives} attempts left to guess the number.")
    lives-=1
    guessed_number = int(input("Make a Guess: "))
    if guessed_number > number:
        print("Too High.\nGuess again.")
    elif guessed_number < number:
        print("Too Low.\nGuess again.")
    else:
        print(f"You guessed it right.The number was : {number}")
        break
if( lives == 0):
    print("You have run out of guesses.You lose.")

