import game_data as gd
import random as rm
import art


def Higher_Lower():
    print(art.higher_lower)
    firs_option_index = rm.randint(0, len(gd.data) - 1)
    firs_option = gd.data[firs_option_index]

    while True:
        second_option_index = rm.randint(0, len(gd.data) - 1)
        if firs_option_index != second_option_index:
            second_option = gd.data[second_option_index]
            break

    game_Controller = True
    score = 0
    while  game_Controller:
        print(f"Compare A: {firs_option["name"]}, a {firs_option["description"]},from {firs_option["city"]}")
        print(art.vs)
        print(f"Compare B: {second_option["name"]}, a {second_option["description"]},from {second_option["city"]}")
        answer = input("Wha has more followers? Type A or B: ")
        is_answer_correct = False
        if firs_option["follower account"] > second_option["follower account"] and answer == "A":
            is_answer_correct = True
        elif firs_option["follower account"] < second_option["follower account"] and answer == "B":
            is_answer_correct = True
        else:
            is_answer_correct = False

        if is_answer_correct:
            score += 1
            print(f"You're right! Current score: {score}\n")
            firs_option = second_option
            firs_option_index = second_option_index
            while True:
                second_option_index = rm.randint(0, len(gd.data) - 1)
                if firs_option_index != second_option_index:
                    second_option = gd.data[second_option_index]
                    break

        else:
            print(f"\nSorry that is wrong! Final score: {score}")
            game_Controller = False

Higher_Lower()