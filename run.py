# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

"""
Game introductory message
"""
def start_game():
    print("===== Welcome to the Hangman Game =====\n")
    select_difficulty()

"""
Inspired by https://github.com/makeuseofcode/Hangman-Game/blob/main/hangman.py
Allows the player to select the difficulty level
"""
def select_difficulty():
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

"""
Selects a word from a list depending on the difficulty level selected
"""
def get_word_from_list(level):



start_game()