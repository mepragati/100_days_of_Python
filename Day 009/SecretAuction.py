import art
import os

def bid_result(auction_details):
  for key in auction_details:
    maximum_bid=auction_details[key]
    winner_name=key
    if(auction_details[key]>maximum_bid):
      maximum_bid = auction_details[key]
      winner_name = key
    print(f"\nCongratulations!! The winner of the Secret Auction is: {winner_name.capitalize()} with bid of ${maximum_bid}.")

auction_continue = True
print(art.logo)
while(auction_continue == True):
    print(art.name)
    auction_list = {}
    name=input("What is your name? ").lower()
    bid_amount=int(input("What is your bid amount? $"))

    auction_list[name]=bid_amount
    user=input("Is there anyone else who want to bid? (yes/no): ").lower()
    if(user == "yes"):
        os.system('cls')
        auction_continue = True
    elif(user =="no"):
        bid_result(auction_list)
        auction_continue = False


