import art
import game_data
import random
import  os

print(art.logo)
ans_is_correct = True 

score =0
while ans_is_correct :
  data_1 = random.choice(game_data.data)
  data_2 = random.choice(game_data.data)

  print(f"\nCompare A: {data_1['name']}, a {data_1['description']}, from {data_1['country']}.")
  print(art.vs)
  print(f"Against B: {data_2['name']}, a {data_2['description']}, from {data_2['country']}.")

  compared_result = 'A' if data_1['follower_count'] > data_2['follower_count'] else 'B'
  user_input = input("\nWho has more followers? Type 'A' or 'B': ").upper()

  if compared_result == user_input :
    score+=1
    print(f"You're right! Current Score: {score}.")
  else:
    os.system('cls')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    ans_is_correct = False

