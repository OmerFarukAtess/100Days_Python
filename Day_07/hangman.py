import random

word_list = ["elma","armut","karpuz","kestane","reçel"]

stages = [
r"""
    *-------*
    |       |
    O       |
   /|\      |
   / \      |
            |
   **************
""",
r"""
    *-------*
    |       |
    O       |
   /|\      |
   /        |
            |
   **************
""",
r"""
    *-------*
    |       |
    O       |
   /|\      |
            |
            |
   ************** 
""",
"""
    *-------*
    |       |
    O       |
   /|       |
            |
            |
   ************** 
""",
"""
    *-------*
    |       |
    O       |
    |       |
            |
            |
   ************** 
""",
"""
    *-------*
    |       |
    O       |
            |
            |
            |
   **************         
""",
"""
    *-------*
    |       |
            |
            |
            |
            |
   **************         
"""]

# TODO-1 Randomly choose a word

choosen_word = random.choice(word_list)
hidden_word_form = []
guessed_word = []

for i in range(len(choosen_word)):
    hidden_word_form.append("_")

lives = 6
is_win = False

while not is_win:
    placeholder = ""

    for i in hidden_word_form:
        placeholder += i

    print(placeholder)
    print(stages[lives])
    print(f"You have {lives} lives")

    if lives == 0:
        print("Game over!!!")
        break

    if placeholder == choosen_word:
        print("You win!!!")
        break

    guess = input("Guess a letter: \n").lower()

    if guess in guessed_word:
        print("You've already guessed this letter")
    else:
        guessed_word.append(guess)
        if guess in choosen_word:
            indices = [i for i, c in enumerate(choosen_word) if c == guess]
            num = 0
            for i in indices:
                hidden_word_form[indices[num]] = choosen_word[i]
                num += 1
        else:
            print("wrong letter")
            lives -= 1








