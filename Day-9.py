# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary :
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > bids[bidder]:
            highest_bidder = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bidder}")


bids ={}
continue_bidding = True
while continue_bidding:
    name = input("what is your name? ")
    price = input("what is your bids? $ ")
    bids[name]=price
    should_continue = input("are there any other bidders? type 'yes' or 'no' ")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

# INI ADALAH SC BY AI AFTER BEDAH dan harus di perbaiki pakai ini
# highest = max(bidding_dictionary.values())
# if bid_amount > highest_bidder:
#     highest_bidder = bid_amount
#     winner = bidder
#     price = int(input(...))
