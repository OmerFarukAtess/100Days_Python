import random as rm

from numpy.ma.core import count

deck = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
playerCards = []
computerCards = []


def getcard():
    index = rm.randint(0, 13)
    card = deck[index]
    return card


def blackJack():
    playerCards.append(getcard())
    playerCards.append(getcard())
    computerCards.append(getcard())
    computerCards.append(getcard())
    gameController = True

    print(f"Your cards: {playerCards}, current score: {sum(playerCards)} ")
    print(f"Computer's first card: {computerCards[0]}")

    while gameController:
        decesion = input("Type 'y' to get another card, type 'n' to pass")

        if decesion == "y":
            playerCards.append(getcard())
            if sum(playerCards) > 21:
                if 11 in playerCards:
                   index11 = playerCards.index(11)
                   playerCards[index11] = 1
                else:
                    gameController = False

        elif decesion == "n":
            print(f"Your cards: {playerCards}, current score: {sum(playerCards)} ")
            print(f"Computer's cards: {computerCards},computer score: {sum(computerCards)}\n")
            while sum(computerCards) < 17:
                computerCards.append(getcard())
                print(f"Your cards: {playerCards}, current score: {sum(playerCards)} ")
                print(f"Computer's cards: {computerCards},computer score: {sum(computerCards)}\n")
            break

        else:
            print("You type wrong letter try again\n")

        print(f"Your cards: {playerCards}, current score: {sum(playerCards)} ")
        print(f"Computer's first card: {computerCards[0]}\n")

    print(f"Your final hand: {playerCards}, final score: {sum(playerCards)} ")
    print(f"Computer's final hand: {computerCards},final score: {sum(computerCards)}\n")

    if sum(playerCards) > 21:
        print("You went over, you lose :)")
    elif sum(playerCards) < sum(computerCards):
        if sum(computerCards) <= 21:
            print("Computer win")
        else:
            print("Computer went over,you win")
    elif sum(playerCards) > sum(computerCards):
        print("You win")

    else:
        print("Draw")




blackJack()

