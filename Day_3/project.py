print("Welvome to Treasue Island.\nYour mission is to find the treasure")
location = input("left or right?")
if location == "left":
    swim = input("swim or wait")
    if swim == "wait":
        door = input("which door? red, blue or yellow")
        if door == "yellow":
            print("You win")
        elif door == "red":
            print("Burned by fire.\nGame Over")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\nGame Over")
else:
    print("Fall into a hole.\nGame Over")