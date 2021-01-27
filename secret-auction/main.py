from art import logo
print(logo)

who_winner_info = {}
should_continue = True

def highest_bidder(record):
    max_score = 0
    winner = ""
    for name in record:
        price = record[name]
        if price > max_score:
            winner = name
            max_score = price
    print(f"winner: {winner}, highest bid: ${max_score}")

while should_continue:
    name = input("Name: ")
    bid = int(input("Bid: $"))
    who_winner_info[name] = bid
    more_bid = input("Are there any other bidders? 'y' or 'n' ")
    if more_bid == "n":
        should_continue = False
        highest_bidder(who_winner_info)