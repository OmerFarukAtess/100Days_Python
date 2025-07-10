from numpy.ma.core import choose

import dataBase as db

def coffe_machine():
    money = 0
    machine_contoller = True
    while machine_contoller:
        selected_option = input("What would you like? (espresso/latte/cappuccino): ")
        if selected_option == "report":
            for key in db.resources:
                print(f"{key}: {db.resources[key]}ml")
            print(f"money ${money}")

        elif selected_option in ["espresso","latte","cappuccino"]:
            resources_check = True
            for key in db.coffees[selected_option]["ingredients"]:
                if db.resources[key] < db.coffees[selected_option]["ingredients"][key]:
                    resources_check = False
                    print(f"Sorry there is not enough {key}")

            if resources_check is False:
                continue
            total = 0
            customer_coin = {
                "penny": 0,
                "dime": 0,
                "nickel": 0,
                "quarter": 0
            }
            print("Please insert coin")
            for key in customer_coin:
                customer_coin[key] = int(input(f"How many {key}: "))

            for key in customer_coin:
                total += customer_coin[key] * db.coin[key]

            if total < db.coffees[selected_option]["cost"]:
                print("Sorry that's not enough money money refunded")
                continue
            else:
                change = round(total - db.coffees[selected_option]["cost"],2)
                money += (total - change)
                print(f"Here is ${change} in change")
                print(f"Here is your {selected_option} Enjoy")
                for key in db.coffees[selected_option]["ingredients"]:
                    db.resources[key] = (db.resources[key] - db.coffees[selected_option]["ingredients"][key])
        elif selected_option == "exit":
            break





coffe_machine()