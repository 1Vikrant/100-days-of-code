import random

# Play the game
options = [0,0,0]

options[0] =  '''
              _______
          ___/   ____)
                 _____)
                 _____)
                 _____)
             ---.____)'''

options[1] =  '''
              ___________
          ___/   ________)_
                   ________)
                 __________)
                 _________)
             ---.________)'''
             
options[2] = '''
              _______
          ___/   ____)____
                   _______)
                 _________)
                 _____)
             ---.____)'''


playing = 'y'

while playing == 'y':

    # Get the choices
    player_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
    computer_chose = random.randint(0, 2)

    print("You chose: ")
    print(options[player_chose])
    print("computer chose: ")
    print(options[computer_chose])

    if player_chose == computer_chose:
        print("Drawn!")
    else:
        if player_chose == 0:
            if computer_chose == 1:
                print(f"Result : You lose!")
            elif computer_chose == 2:
                print("Result: You Win!")
        if player_chose == 1:
            if computer_chose == 0:
                print("Result: You Win")
            elif computer_chose == 2:
                print("Result: You lose")
        if player_chose == 2:
            if computer_chose == 0:
                print("You lose")
            elif computer_chose == 1:
                print("You Win.")
    playing = input("enter 'y' to play more")

print("Thanks for visiting")
