# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import sys
import os
from colorama import init
from colorama import Fore
from colorama import Back
from colorama import Style
init()


def start_game():
    """
    Game introductory message
    """
    os.system('clear')
    print(Style.BRIGHT + "\n===== Welcome to the Hangman Game =====\n")
    select_difficulty()


def select_difficulty():
    """
    Allows the player to select the difficulty level
    """
    while True:
        choice = input(Style.NORMAL + "Write 'easy', 'medium' or 'hard' level, or 'instructions':\n")

        if 'easy' in choice.lower():
            print(Fore.BLUE + "You selected easy")
            print(Fore.RESET + "\n")
            level = 'easy'
            get_word_from_list(level)

        elif 'medium' in choice.lower():
            print(Fore.YELLOW + "You selected medium")
            print(Fore.RESET + "\n")
            level = 'medium'
            get_word_from_list(level)

        elif 'hard' in choice.lower():
            print(Fore.RED + "You selected hard")
            print(Fore.RESET + "\n")
            level = 'hard'
            get_word_from_list(level)
        elif 'instructions' in choice.lower():
            check_instructions()
            continue
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
            filtered_list = [i for i in wordlist if len(i) <= 5]
        elif level == 'medium':
            filtered_list = [i for i in wordlist if len(i) > 5 & len(i) <= 10]
        elif level == 'hard':
            filtered_list = [i for i in wordlist if len(i) > 10]

    word = random.choice(filtered_list)
    run_game(word)


def draw_hangman(chances):
    """
    Inspired by
    https://github.com/makeuseofcode/Hangman-Game/blob/main/hangman.py
    It shows the hangman depending on how many chances the player has left
    """
    if chances == 6:
        os.system('clear')
        print(" ________      ")
        print(" |      |      ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print(Back.WHITE + Fore.WHITE + "¯¯¯¯¯          ")
        print(Back.RESET + "\n")
    elif chances == 5:
        os.system('clear')
        print(Fore.CYAN + " ________      ")
        print(Fore.CYAN + " |      |      ")
        print(Fore.CYAN + " |      0      ")
        print(Fore.CYAN + " |             ")
        print(Fore.CYAN + " |             ")
        print(Fore.CYAN + " |             ")
        print(Back.CYAN + Fore.CYAN + "¯¯¯¯¯          ")
        print(Back.RESET + Fore.RESET + "\n")
    elif chances == 4:
        os.system('clear')
        print(Fore.BLUE + " ________      ")
        print(Fore.BLUE + " |      |      ")
        print(Fore.BLUE + " |      0      ")
        print(Fore.BLUE + " |     /       ")
        print(Fore.BLUE + " |             ")
        print(Fore.BLUE + " |             ")
        print(Back.BLUE + Fore.BLUE + "¯¯¯¯¯          ")
        print(Back.RESET + Fore.RESET + "\n")
    elif chances == 3:
        os.system('clear')
        print(Fore.YELLOW + " ________      ")
        print(Fore.YELLOW + " |      |      ")
        print(Fore.YELLOW + " |      0      ")
        print(Fore.YELLOW + " |     /|      ")
        print(Fore.YELLOW + " |             ")
        print(Fore.YELLOW + " |             ")
        print(Back.YELLOW + Fore.YELLOW + "¯¯¯¯¯          ")
        print(Back.RESET + Fore.RESET + "\n")
    elif chances == 2:
        os.system('clear')
        print(Fore.MAGENTA + " ________      ")
        print(Fore.MAGENTA + " |      |      ")
        print(Fore.MAGENTA + " |      0      ")
        print(Fore.MAGENTA + " |     /|\\    ")
        print(Fore.MAGENTA + " |             ")
        print(Fore.MAGENTA + " |             ")
        print(Back.MAGENTA + Fore.MAGENTA + "¯¯¯¯¯          ")
        print(Back.RESET + Fore.RESET + "\n")
    elif chances == 1:
        os.system('clear')
        print(Fore.RED + " ________      ")
        print(Fore.RED + " |      |      ")
        print(Fore.RED + " |      0      ")
        print(Fore.RED + " |     /|\\    ")
        print(Fore.RED + " |     /       ")
        print(Fore.RED + " |             ")
        print(Back.RED + Fore.RED + "¯¯¯¯¯          ")
        print(Back.RESET + Fore.RESET + "\n")
    elif chances == 0:
        os.system('clear')
        print(Fore.RED + " ________      ")
        print(Fore.RED + " |      |      ")
        print(Fore.RED + " |      0      ")
        print(Fore.RED + " |     /|\\    ")
        print(Fore.RED + " |     / \\    ")
        print(Fore.RED + " |             ")
        print(Back.RED + Fore.RED + "¯¯¯¯¯          ")
        print(Back.RESET + Fore.RESET + "\n")


def run_game(word):
    """
    Takes the randomly selected word according to difficulty level
    and use it in a loop where the player can try to find the solution
    """
    temp = get_some_letters(word)
    chances = 7
    found = False
    while True:
        if chances == 0:
            print(Fore.RED + f"Game Over! The word was: {word}")
            gameOver_check = True
            while gameOver_check == True:
                gameOver_choice = input(Fore.RESET + "Do you want to play again? (Write 'yes' or 'no'):\n")
                if 'yes' in gameOver_choice.lower():
                    gameOver_check = False
                    start_game()
                elif 'no' in gameOver_choice.lower():
                    print('Quitting the game...')
                    gameOver_check = False
                    sys.exit()
                else:
                    os.system('clear')
                    print("Please enter a valid choice.")
                    print("\n")
        print(Style.BRIGHT + "==== Guess the word ====\n")
        print(Style.NORMAL + temp, end='')
        print(f"\t(word has {len(word)} letters)")
        print(f"Chances left: {chances}")
        character = input("Write a letter, 'restart' or 'instructions':\n")
        if len(character) > 1 or not character.isalpha():
            if ("restart" in character.lower()):
                start_game()
            elif ("instructions" in character.lower()):
                check_instructions()
                continue
            else:
                os.system('clear')
                print("Write a single letter only or 'restart' to start again")
                continue
        else:
            for num, char in enumerate(list(word)):
                if char == character.lower():
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
        if found:
            found = False
        else:
            chances -= 1
        if '_' not in temp:
            print(Fore.GREEN + f"\nYou Won! The word was: {word}")
            gameWon_check = True
            while gameWon_check == True:
                gameWon_choice = input(Fore.RESET + "Do you want to play again? (Write 'yes' or 'no'):\n")
                if 'yes' in gameWon_choice.lower():
                    gameWon_check = False
                    start_game()
                elif 'no' in gameWon_choice.lower():
                    print('Quitting the game...')
                    gameWon_check = False
                    sys.exit()
                else:
                    os.system('clear')
                    print("Please write a valid choice.")
                    print("\n")
        else:
            draw_hangman(chances)
        print()


def check_instructions():
    """
    Game Instructions
    """
    os.system('clear')
    print(Back.CYAN + Style.BRIGHT + "INSTRUCTIONS:")
    print(Back.RESET + Style.NORMAL + "- The goal of the game is to guess the mysterious word")
    print("before the man is hanged.")
    print("- Write one of the 3 difficulty levels (easy, medium or hard).")
    print("The difference is the lenght of the words.")
    print("- You can guess only one letter at a time.")
    print("- You have 7 opportunities to make mistakes.")
    print("- If you guess the word, you will win and save the man.")
    print("- You can anytime restart the game typing 'restart'")
    print("- Only one letter is accepted per try.\n")


def get_some_letters(word):
    """
    Inspired by
    https://github.com/makeuseofcode/Hangman-Game/blob/main/hangman.py
    It takes the selected word for the game and converts it into a
    set of '_' marks
    """
    letters = []
    temp = '_'*len(word)
    for char in list(word):
        if char not in letters:
            letters.append(char)
    character = random.choice(letters)
    for num, char in enumerate(list(word)):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp


start_game()
