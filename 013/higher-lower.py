from art import logo, vs
from game_data import data
import random
from os import system

def game():
    person1 = random.choice(data)
    score = 0
    end_game = False
    while not end_game:
        person2 = random.choice(data)
        while person1 == person2:
            person2 = random.choice(data)

        print("\n")
        print(f"{person1['name']} is a {person1['description']} from {person1['country']}.")
        print(vs)
        print(f"{person2['name']} is a {person2['description']} from {person2['country']}.")
        print("\n")

        if person1['follower_count'] > person2['follower_count']:
            answer = "l"
        else:
            answer = "h"
        guess = input("higher/lower? (h/l): ")


        if answer == guess:
            score += 1
            person1 = person2
        else:
            end_game = True
            print(f"{person1['name']} : {person1['follower_count']}")
            print(f"{person2['name']}: {person2['follower_count']}")
        print(f"Your score: {score}")
    return 0

while input("Do you want to play a game?(y/n): ") == 'y':
    system("clear")
    print(logo)
    game()