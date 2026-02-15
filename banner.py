
import os
import subprocess
import sys
import platform
import questionary
from questionary import Style

def banner():
    GREEN = "\033[32m"
    RED = "\033[31m"
    Cyan = "\033[36m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    RESET = "\033[0m"

    font = f"""{Blue}
    
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗███████╗    
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝    
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗  ███████╗    
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║    
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║    
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝    
                                                                                                         
    
    """
    print(font)

def run_game(game_folder):
    try:
        if platform.system() == "Windows":
            os.system(f'cd "{game_folder}" && "{sys.executable}" main.py')
        else:
            os.system(f'cd "{game_folder}" && "{sys.executable}" main.py')
    except Exception as e:
        print(f"Error running game: {e}")

# Available games mapping: display name -> folder name
games = {
    "BlackJack": "BlackJack",
    "Breakout": "Breakout",
    "Hangman": "Hangman",
    "KBC": "KBC",
    "Pacman": "Pacman",
    "PingPong": "PingPong",
    "RockPaperScissor": "RockPaperScissor",
    "SnakeGame": "SnakeGame",
    "TurtleCrossing": "TurtleCrossing"
}


def main():
    blue_menu_style = Style([
        ('qmark', 'fg:#673ab7 bold'),
        ('question', 'bold'),
        ('answer', 'fg:#2196f3 bold'),
        ('pointer', 'fg:#673ab7 bold'),
        ('highlighted', 'fg:#2196f3 bold'),
        ('selected', 'fg:#cc5454'),
        ('separator', 'fg:#cc5454'),
        ('instruction', ''),
        ('text', ''),
        ('disabled', 'fg:#858585 italic')
    ])

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        
        choices = list(games.keys()) + ["Exit"]
        
        choice = questionary.select(
            "Select a Game to Play:",
            choices=choices,
            style=blue_menu_style,
            use_indicator=True
        ).ask()

        if choice == "Exit":
            sys.exit()
        
        if choice in games:
            game_folder = games[choice]
            print(f"Starting {game_folder}...")
            run_game(game_folder)
            input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
