import random

roll = random.randint(1, 6)
guess = int(input("Guess the dice roll:\n"))

if guess == roll:
    print("You guessed correctly! They rolled a " + str(roll))
else:
    print("You guessed incorrectly! They rolled a " + str(roll))
