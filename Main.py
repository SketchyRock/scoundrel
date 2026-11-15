import sys

if sys.version_info < (3, 10):
    sys.exit("Scoundrel needs Python 3.10 or newer.")

import Display
import Handling
from GameState import GameState


def main_loop():
    """Show the main menu forever; each pass starts from a fresh GameState."""
    while True:
        state = GameState()
        Display.print_main_menu()
        Handling.menu_input(Handling.COMMANDS_main, state)


if __name__ == "__main__":
    main_loop()
