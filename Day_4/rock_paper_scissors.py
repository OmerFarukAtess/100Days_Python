import random as rm
from random import random

rock =  """
    _______
---'   ____)            
      (_____)       
      (_____)       
      (____)        
---.__(___)
"""

paper = """
    _______         
---'   ____)____    
          ______)   
          _______)
         _______)                           
---.__________)   
"""

scissors = """
     _______         
---'   ____)____
          ______)       
       __________)  
      (____)        
---.__(___)
"""

game_images = [rock,paper,scissors]

print("Welcom to rock paper scissors game")
player_choose = int(input("Please choose a number? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
computer_choose = rm.randint(0,2)

print(f"You choose\n {game_images[player_choose]}")

print(f"Computer choose\n {game_images[computer_choose]}")

if player_choose == 0  and computer_choose == 0:
    print("Draw")
elif player_choose == 0 and computer_choose == 1:
    print("You lose")
elif player_choose == 0 and computer_choose == 2:
    print("You win")
elif player_choose == 1  and computer_choose == 1:
    print("Draw")
elif player_choose == 1 and computer_choose == 2:
    print("You lose")
elif player_choose == 1 and computer_choose == 0:
    print("You win")
elif player_choose == 2  and computer_choose == 2:
    print("Draw")
elif player_choose == 2 and computer_choose == 0:
    print("You lose")
elif player_choose == 2 and computer_choose == 1:
    print("You win")
else:
    print("You typed a invalid number")

