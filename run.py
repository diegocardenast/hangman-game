# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def start_game():
    """
    Game introductory message
    """
    print("===== Welcome to the Hangman Game =====\n")
    select_difficulty()


def select_difficulty():
    """
    Allows the player to select the difficulty level
    """
    while True:
        choice = input("Please select the difficulty level (easy/medium/hard): ")
        
        if 'easy' in choice.lower():
            print("You selected easy")
            print("\n")
            level = 'easy'
            get_word_from_list(level)
            
        elif 'medium' in choice.lower():
            print("You selected medium")
            print("\n")
            level = 'medium'
            get_word_from_list(level)
            
        elif 'hard' in choice.lower():
            print("You selected hard")
            print("\n")
            level = 'hard'
            get_word_from_list(level)
              
        else:
            print("Please enter a valid choice.")
            print("\n")


def get_word_from_list(level):
    """
    Selects a word from a list depending on the difficulty level selected
    """
    wordlist = []
    with open("hangman_wordlist.txt", 'r') as file:
        wordlist = file.read().split('\n')

        if level == 'easy':
            filtered_list = [ i for i in wordlist if len(i)<= 5]
        elif level == 'medium':
            filtered_list = [ i for i in wordlist if len(i)> 5 & len(i)<= 10]
        elif level == 'hard':
            filtered_list = [ i for i in wordlist if len(i)> 10]

    word = random.choice(filtered_list)
    print(len(filtered_list))
    print(word)
    return word


start_game()