import random
import hangman_stages
word_list = ["canada","india","switzerland","california","england"]
chosen_word=random.choice(word_list)
# print(chosen_word)

display=[]
for i in range(len(chosen_word)):
    display+="_"
print(display)

lives=6

game_over=False
while not game_over:
    guessed_letter = input("Guess the letter: ")  # i,n,d,i,a
    for position in range(len(chosen_word)):  # 0,1,2,3,4,5,....,n   #It will check each letter on each position
        letter = chosen_word[position]     # letter is present in the chosen word.
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1
    if lives==0:
        game_over=True
        print()
        print('You lose, Better luck next time...')

    if "_" not in display:
        game_over = True
        print()
        print("Congratulations, You won!!!")
    print(hangman_stages.stages[lives])




