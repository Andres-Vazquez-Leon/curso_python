"""Text user interface for the tournament using colorama."""
from colorama import Fore, Back, Style, init
init(autoreset=True)

class ColoramaUI:

    def __init__(self):
        self.tournament = None
        self.current_file = None

    def set_current_file(self, file_path: str):
        self.current_file = file_path
    
    def run (self):
        """Run the colorama UI."""
        colorama.init(autoreset=True)
        self.show_menu()

    def show_menu(self):
        """Show the menu"""
        while True:
            print(f"\nTournament)")
            print("1. Load tournament")
            print("2. Display tournament")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                file_path = input("Enter the path to the tournament JSON file: ")
                self.set_current_file(file_path)
                self.open_tournament(file_path)
            elif choice == "2":
                self.display_tournament()
            elif choice == "3":
                self.exit_app()
            else:
                print("Invalid choice. Please try again.")
                break
    
    def open_tournament(self, file_path: str):
        """Open tournament from JSON file."""


    def display_tournament(self):
        