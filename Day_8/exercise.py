def calculate_love_score(name1, name2):
    true_love = {"T": 0, "R": 0, "U": 0, "E": 0, "L": 0, "O": 0, "V": 0}

    for i in name1.lower():
        if i.lower() == "t":
            true_love["T"] += 1
        elif i.lower() == "r":
            true_love["R"] += 1
        elif i.lower() == "u":
            true_love["U"] += 1
        elif i.lower() == "e":
            true_love["E"] += 1
        elif i.lower() == "l":
            true_love["L"] += 1
        elif i.lower() == "o":
            true_love["O"] += 1
        elif i.lower() == "v":
            true_love["V"] += 1
        elif i.lower() == "e":
            true_love["E"] += 1

    for i in name2.lower():
        if i.lower() == "t":
            true_love["T"] += 1
        elif i.lower() == "r":
            true_love["R"] += 1
        elif i.lower() == "u":
            true_love["U"] += 1
        elif i.lower() == "e":
            true_love["E"] += 1
        elif i.lower() == "l":
            true_love["L"] += 1
        elif i.lower() == "o":
            true_love["O"] += 1
        elif i.lower() == "v":
            true_love["V"] += 1
        elif i.lower() == "e":
            true_love["E"] += 1


    total1 = true_love["T"] + true_love["R"] + true_love["U"] + true_love["E"]
    total2 = true_love["L"] + true_love["O"] + true_love["V"] + true_love["E"]
    total3 =int(f"{total1}{total2}")

    print(total3)

calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")