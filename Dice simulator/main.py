# Dice simulator python project By Rahul Thakur
import random
again = True
while again:
    print(random.randint(1,6))
    another_roll=input("do u want to roll the dice (y/n): ")
    if another_roll.lower()=="y":
        continue
    else:
        break

