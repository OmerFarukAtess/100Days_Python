import random as rm
import art

def guessNumber():
    print(art.start)
    print("Welcome to the number guessing game\n"
          "I am thinking a number between 1 and 100")
    attempts = 0
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            attempts = 10
            break
        elif difficulty == 'hard':
            attempts = 5
            break
        else:
            print("undefined difficulty , try again.")

    number = rm.randint(1,100)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! Answer is {number}.")
            break
        elif guess < number:
            attempts -= 1
            if attempts == 0:
                print("To low.\n"
                      "You run out of guesses, you lose.\n"
                      f"Correct number is {number}")
            else :
                print("To low.\n"
                      "Guess again.")
        else:
            attempts -= 1
            if attempts == 0:
                print("To high\n"
                      "You run out of guesses, you lose.\n"
                      f"Correct number is {number}")
            else:
                print("To high.\n"
                      "Guess again.\n")


guessNumber()


