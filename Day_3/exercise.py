print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperonni = input("Do you want pepporonni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_amount = 0

if size == "S":
    total_amount += 15
elif size == "M":
    total_amount +=20
elif size == "L" :
    total_amount +=25
else:
    print("You typed wrong inputs.")

if pepperonni == "Y":
    if size == "S":
        total_amount +=2
    elif size == "M" or size == "L":
        total_amount +=3


if extra_cheese == "Y":
    total_amount +=1

print(f"Total amount: {total_amount}")