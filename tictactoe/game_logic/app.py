"""
TicTacToe Game
Author: Andrés Manuel Vazquez León
"""
from game_logic import game
from menu import display_menu
from game_logic import two_players

def main():
    while True:
        choice = display_menu()
        if choice == 1 :
            print("One Player Game is not implemented yet")
            #here you woul call one player game function when implement
        elif choice == 2:
            two_players()
        elif choice == 3:
            print("Exiting the game: Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option")


if __name__ == "__main__":
    main()