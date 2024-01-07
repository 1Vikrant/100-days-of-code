from random import randint

print("Welcome!")
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def play():
    answer = randint(1, 100)
    level = input("select difficuty: ")
    if level == "hard":
        turns = HARD_LEVEL_TURNS
    else:
        turns = EASY_LEVEL_TURNS

    while turns > 0:
        print(f"You have {turns} attempts left.")
        guess = int(input("Guess a number: "))
        if guess == answer:
            print("win")
            turns = 0
        elif guess < answer:
            print("too low")
            turns -= 1
        else:
            print("too high")
            turns -= 1
    if turns == 0 and guess != answer:
        print(f"You lose!!The number is {answer}")
    while input("Do you want to play more(y/n): ") == 'y':
        from os import system
        system("clear")
        play()
    return
    
play()