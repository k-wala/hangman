import random

word_list = ["mango", "kiwi", "watermelon", "strawberry", "grapefruit"]

class Hangman():
    '''
    This class codes the logic for the game hangman.
    
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = list("_" * len(self.word))
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        '''
        Initialising additional attributes:

        Attributes:
            word: the word to be guessed chosen at random from the word_list
            word_guessed: a list of "_" with each underscore replaced for every 
            correct letter guessed
            num_letters: the number of unique letters in the word
            list_of_guesses: a list of all the guessed letters by the user
    
        '''
    
    def check_guess(self, guess):
        '''
        This method checks whether the guessed letter is in the word.
        
        If it is:
        The letter is added to word_guessed
        The num_letters is reduced by one 

        If it isn't:
        The num_lives is reduced by one
        The user gets to try again

        Parameters:
            guess: the user input from the ask_for_input method 
    
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives remaining.")
    
    def ask_for_input(self):
        '''
        This method asks the user for input (a letter) and validates if the user 
        has entered one character and if that character is an alphabetical value. 

        If it isn't:
        The user gets an error message and is prompted to try again

        If the user has entered a repeat letter:
        The user gets an error message and is prompted to try again

        If it is:
        The letter is added to the list_of_guesses attribute 
        The check_guess method is called to check if the input is in the word

        '''
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) > 1 or guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    '''
    This function takes in the word_list as an argument and forms the logic 
    of the game. 

    Parameters:
        word_list: the list of possible words from which the word is randomly 
        chosen 

    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif num_lives != 0 and game.num_letters == 0:
            print(f"You won! The word is {game.word}.")
            break

play_game(word_list)