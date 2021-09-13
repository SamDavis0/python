#NINE LIVES GAME
import random
words = ["handy", "issue", "brush", "shaft", "grain", "pound"]

secret_word = random.choice(words)

clue = list("?")

heart_symbol = u'\u2764'

hearts = [heart_symbol, heart_symbol, heart_symbol, heart_symbol, heart_symbol, heart_symbol, heart_symbol, heart_symbol, heart_symbol]

secret_word_list = list(f'{secret_word}')

index = ""
lives = 9
while lives > 0:
    fails = 0
    for x in secret_word:
        if x in index:
            print(x)
        else:
            print(clue)
            fails += 1
    if fails == 0:
        print("Congratulations", secret_word, "is correct!")
        break
    print(hearts)
    answer = input("Guess a letter: ")
    index += answer
    if answer not in secret_word:
        lives -= 1
        hearts.pop()
        print("You lost a life")
        if lives == 0:
            print("You Lose")