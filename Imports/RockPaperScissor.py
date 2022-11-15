import random

computer_choice = random.choice(['scissors', 'paper', 'rock'])

user_choice = input('Do you want to - rock, paper, or scissors:\n')

if computer_choice == user_choice:
    print('Tie!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win! The computer chose ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win! The computer chose ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win! The computer chose ' + computer_choice)
else:
    print('You lose :( Computer Wins :D! The computer chose ' + computer_choice)