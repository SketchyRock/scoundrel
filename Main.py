import Display
import Handling
from GameState import GameState

# - finish win and lose condition, risk your current score for more in the next run
# - create a stats page
# - later implement a classic mode or a base building rougelite mode that uses score as currency
# - make all text appear on screen using display_text() func


def main_loop():
    """Major overarching loop,
    returns player to main menu if they exit the game loop,
    initializes GameState"""
    #initialize stats, later on create a file and pull data from it

    while True:
        state = GameState()
        Display.print_main_menu()
        Handling.menu_input(Handling.COMMANDS_main, state)


if __name__ == "__main__":
    main_loop()
