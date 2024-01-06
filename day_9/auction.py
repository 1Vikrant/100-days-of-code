bids = {

}

def add_bid(name, bid):
    bids[name] = bid

def declare_winner(bids):
    winner = ""
    max_bid = 0
    for key in bids:
        if bids[key] > max_bid:
            max_bid = bids[key]
            winner = key
    return winner

play = True
while play:
    print("Welcome")
    name = input("name?: ")
    bid = int(input("bid?: "))
    add_bid(name, bid)
    moreplay = input("more bidders?: ")
    if moreplay != "yes":
        play = False

print(bids)
print(f"And the winner is {declare_winner(bids)}")