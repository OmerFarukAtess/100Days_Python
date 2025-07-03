import random
from pickle import PROTO

print("Welcome to heads tails program")
input("When you ready press a key")
H_T = random.randint(0,1)
if H_T == 0:
    print("HEADS")
elif H_T == 1:
    print("TAILS")
