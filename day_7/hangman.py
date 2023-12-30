#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"The word was {chosen_word}.")
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])






'''import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
lives = 6
display = []

# Choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#test code
print(chosen_word)

# Create blanks
for _ in range(word_length):
    display += "_"
print(display)

print(logo)

while not end_of_game:

    #ask player to guess
    guess = input("Guess a letter: ")

    if guess in display:
        print(f"You already guessed the letter {guess}.")
    else:
        #check if guess is in the chosen word
        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        #Check if guess was in the chose word
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("you lose.")
    
    print(''.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])'''



'''sequence = ["__"]*len(word)
while lives:
    print(f'{"".join(sequence)}')
    guess = input("Guess a letter: ")
    for index in range(len(word)):
        if guess == word[index]:
            match = True
            sequence[index] = guess
    if "".join(sequence) == word:
        lives = 0
        print(f"You guessed it. The word is {word}.")
        print("You win!!!!!!")
    if not match:
        lives -= 1
        print(f"You guessed {guess} that's not in the word. You lose a life.")
        print("HANGMAN"[:7-lives])
    
    match = False'''
