
import random
from Hangman_word_list import word_list

#Generate a random word from a predefinded list :
chosen_word = random.choice(word_list)
print(chosen_word)

#Take the length of the random word and create dashes same number of time.
display=[]
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"




end_of_game = False
lives = 6

from HangMan_Art import logo
print(logo)

while not end_of_game:
    
   # Taking each letter and checking whether it matches with the selected random word
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f'You have already guessed the word {guess}')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    

    #To check number of  lives left
    if guess not in chosen_word:
        lives -= 1
        print(f'U have {lives} lives left')
        if lives == 0:
            end_of_game = True
            print("You Loose")

    if "_" not in display:
        end_of_game = True
        print("You Win")


    from HangMan_Art import stages
    print(stages[lives])
