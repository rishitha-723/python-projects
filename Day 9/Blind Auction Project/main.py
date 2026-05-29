import art
print(art.logo)
# TODO-1: Ask the user for input
bids = False
blind_auction = {}
while not bids:
    name = input("Enter name: ")
    bid = int(input("Enter bid amount: "))
    # TODO-2: Save data into dictionary {name: price}
    blind_auction[name] = bid
    # TODO-3: Whether if new bids need to be added
    bids = input("Any other user for auction yes or no ?").lower()
    if bids == "yes":
        bids = False
        print("\n" * 10)
    else:
        bids = True
    # TODO-4: Compare bids in dictionary
high = 0
for key in blind_auction:
    if blind_auction[key] > high:
        high = blind_auction[key]
print("Highest bid $ ", high)



