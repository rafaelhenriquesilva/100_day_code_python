# The secret Auction Program Instructuons and Flow chart
print('Welcome to the secret auction program.')

continue_program = True

dictionaries_bid = {}

while continue_program:
    username = input("What's your name?: ")
    user_bid = float(input("What's your bid?: $"))
    dictionaries_bid[username] = user_bid
    decision = input("Are there any bidders? Type 'yes' or 'no' ")
    if not decision == "yes":
        continue_program = False

max_value = 0
mapping_better_bid = {}     
for key in dictionaries_bid:
    if(dictionaries_bid[key] > max_value):
        mapping_better_bid = {}  
        max_value = dictionaries_bid[key]
        mapping_better_bid[key] = dictionaries_bid[key]
        
for key in mapping_better_bid:
    print(f"The {key} did the better bid, value: ${mapping_better_bid[key]}  ")