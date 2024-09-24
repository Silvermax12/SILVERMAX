import os

logo = """
                                    ,.ood888888888888boo.,
                               .od888P^""            ""^Y888bo.
                           .od8P''   ..oood88888888booo.    ``Y8bo.
                        .odP'"  .ood8888888888888888888888boo.  "`Ybo.
                      .d8'   od8'd888888888f`8888't888888888b`8bo   `Yb.
                     d8'  od8^   8888888888[  `'  ]8888888888   ^8bo  `8b
                   .8P  d88'     8888888888P      Y8888888888     `88b  Y8.
                  d8' .d8'       `Y88888888'      `88888888P'       `8b. `8b
                 .8P .88P            """"            """"            Y88. Y8.
                 88  888                                              888  88
                 88  888                                              888  88
                 88  888.        ..                        ..        .888  88
                 `8b `88b,     d8888b.od8bo.      .od8bo.d8888b     ,d88' d8'
                  Y8. `Y88.    8888888888888b    d8888888888888    .88P' .8P
                   `8b  Y88b.  `88888888888888  88888888888888'  .d88P  d8'
                     Y8.  ^Y88bod8888888888888..8888888888888bod88P^  .8P
                      `Y8.   ^Y888888888888888LS888888888888888P^   .8P'
                        `^Yb.,  `^^Y8888888888888888888888P^^'  ,.dP^'
                           `^Y8b..   ``^^^Y88888888P^^^'    ..d8P^'
                               `^Y888bo.,            ,.od888P^'
                                    "`^^Y888888888888P^^'"         LS
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder(bidding_dictionary):
    # Find the bidder with the maximum bid
    richest_bidder = max(bidding_dictionary, key=bidding_dictionary.get)
    highest_bid = bidding_dictionary[richest_bidder]
    print(f"The winner is {richest_bidder} with a bid of ${highest_bid}.")

bids = {}
more_bidders = True

while more_bidders:
    print(logo)
    name = input("What's your name? ")
    price = int(input("How much do you wanna bid? $"))
    bids[name] = price

    should_continue = input("Are there any more bidders? Y/N: \n").upper()
    if should_continue == "N":
        more_bidders = False
        highest_bidder(bids)
    elif should_continue == "Y":
        clear()
