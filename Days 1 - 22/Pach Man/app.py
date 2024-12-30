import random
from packman import hangman_states

words = ["luminous", "wanderlust", "serendipity", "ephemeral", "quixotic"]
chosen_word = random.choice(words)
display =[]
lives = 7

print(chosen_word)
for _ in chosen_word:
    display += '_'
# temp_lives = 0
print(hangman_states[0])
guess = input("Guess a letter please? ").lower()[0]
end_of_game = False

while not end_of_game:
    print(hangman_states[-lives])
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lost")
            end_of_game = True
    print("Lives left: ", lives)
    print(display)
    if '_' in display:
        guess = input("Guess a letter please? ").lower()
    else :
        print("You win")
        end_of_game = True