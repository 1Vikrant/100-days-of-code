import random

rock =  '''
              ROCK
             ______
        ____/   ___)_
                _____)
                _____)
        _______ ____)
               \___)'''

paper =  '''
                PAPER
             ____________
        ____/   _________)_
                ___________)
                ___________)
        _______ ___________)
               \_________)'''
             
scissor = '''
               SCISSOR
              _______
        _____/  _____)_____
                ___________)
                ___________)
        _______ _______)
               \_____)'''

player_choices = [0, 1, 2]
options = [rock, paper, scissor]

playing = 'y'

while playing.lower() == 'y':
    #player's turn
    invalid = True
    while invalid:
        player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
        if player_choice in player_choices:
            invalid = False
        else:
            print("Please enter a valid choice[0/1/2]")

    # Computer's Turn
    computer_choice = random.randint(0, 2)

    print("You chose: ")
    print(options[player_choice])
    print("computer chose: ")
    print(options[computer_choice])

    if player_choice == computer_choice:
        print("Drawn!")
    else:
        if player_choice == 0:
            if computer_choice == 1:
                print("Result : You lose!")
            elif computer_choice == 2:
                print("Result: You Win!")
        if player_choice == 1:
            if computer_choice == 0:
                print("Result: You Win")
            elif computer_choice == 2:
                print("Result: You lose")
        if player_choice == 2:
            if computer_choice == 0:
                print("You lose")
            elif computer_choice == 1:
                print("You Win.")
    playing = input("enter 'y' to play more: ")

print("Thanks for visiting")
