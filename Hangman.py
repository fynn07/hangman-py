import random
import os
import hangman_art
import hangman_words

display = []

chosen_word = random.choice(hangman_words.word_list)
for letter in chosen_word:
    display.append('_')

life = 5
flag = 0

print(hangman_art.logo)

start = input("Enter any key to start: ")

while('_' in display):
    os.system('cls')
    print(f"{' '.join(display)}")
    print(hangman_art.stages[life])
    
    print(f"Life: {life}")
    guess = input("Guess a letter: ").lower()
    indeces = 0
    
    for letter in chosen_word:

        if letter == guess:
            display[indeces] = letter
            flag += 1
        indeces += 1
    
    if flag == 0:
        life -= 1
    flag = 0
    if life == 0:
        os.system('cls')
        print(hangman_art.stages[life])
        print("You Lose.")
        print(f"The word was: {chosen_word}!")
        break

if (life > 0):
    print("You Win!")