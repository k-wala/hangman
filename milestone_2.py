import random

word_list = ["mango", "kiwi", "watermelon", "strawberry", "satsuma"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please guess a letter: ")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That's not a valid input.")
    