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
    run_game(word)


def draw_hangman(chances):
    """
    Inspired by https://github.com/makeuseofcode/Hangman-Game/blob/main/hangman.py
    It shows the image of the hangman depending on how many chances the player has left
    """
    if chances == 6:
        print(" ________      ")
        print(" |      |      ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print("¯¯¯¯¯          ")
    elif chances == 5:
        print(" ________      ")
        print(" |      |      ")
        print(" |      0      ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print("¯¯¯¯¯          ")
    elif chances == 4:
        print(" ________      ")
        print(" |      |      ")
        print(" |      0      ")
        print(" |     /       ")
        print(" |             ")
        print(" |             ")
        print("¯¯¯¯¯          ")
    elif chances == 3:
        print(" ________      ")
        print(" |      |      ")
        print(" |      0      ")
        print(" |     /|      ")
        print(" |             ")
        print(" |             ")
        print("¯¯¯¯¯          ")
    elif chances == 2:
        print(" ________      ")
        print(" |      |      ")
        print(" |      0      ")
        print(" |     /|\     ")
        print(" |             ")
        print(" |             ")
        print("¯¯¯¯¯          ")
    elif chances == 1:
        print(" ________      ")
        print(" |      |      ")
        print(" |      0      ")
        print(" |     /|\     ")
        print(" |     /       ")
        print(" |             ")
        print("¯¯¯¯¯          ")
    elif chances == 0:
        print(" ________      ")
        print(" |      |      ")
        print(" |      0      ")
        print(" |     /|\     ")
        print(" |     / \     ")
        print(" |             ")
        print("¯¯¯¯¯          ")


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
            print(f"Game Over! The word was: {word}")
            gameOver_choice = input("Do you want to try again? (yes/no): ")
            while True:
                if 'yes' in gameOver_choice.lower():
                    start_game()
                elif 'no' in gameOver_choice.lower():
                    print('Quitting the game...')
                    break
                else:
                    print("Please enter a valid choice.")
                    print("\n")

        print("=== Guess the word ===")
        print(temp, end='')
        print(f"\t(word has {len(word)} letters)")
        print(f"Chances left: {chances}")
        character = input("Enter the character you think the word may have (or 'restart' to start again): ")
        if len(character) > 1 or not character.isalpha():
            if(character == "restart"):
                start_game()
            else:
                print("Please enter a single alphabet only or 'restart' start again")
                continue
        else:
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
        if found:
            found = False
        else:
            chances -= 1
        if '_' not in temp:
            print(f"\nYou Won! The word was: {word}")
            print(f"You got it in {7 - chances} guess")
            gameWon_choice = input("Do you want to play again? (yes/no): ")
            while True:
                if 'yes' in gameWon_choice.lower():
                    start_game()
                elif 'no' in gameWon_choice.lower():
                    print('Quitting the game...')
                    break
                else:
                    print("Please enter a valid choice.")
                    print("\n")
        else:
            draw_hangman(chances)
        print()


def get_some_letters(word):
    """
    Inspired by https://github.com/makeuseofcode/Hangman-Game/blob/main/hangman.py
    It takes the selected word for the game and converts it into a set of '_' marks
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