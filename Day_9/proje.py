persons = {}

def find_higger_bid():
    maximum_bid = max(persons.values())
    winner = ""

    for key in persons:
        if persons[key] == maximum_bid:
            winner = key

    print(f"the winner is {winner}")

while 1:
    name = input("what is your name: ")
    bid = input("what is your bid: ")
    persons[name] = bid

    answer = input("Are there any other bidders? Type 'yes' or 'no' ")
    if answer == "no":
        break

find_higger_bid()

