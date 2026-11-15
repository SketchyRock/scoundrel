from sys import exit
import Game
import Display

def show_guide(state) -> None:
    Display.print_full_guide()


def quit_game(state) -> None:
    exit()


COMMANDS_main = {
    "1": Game.game_loop,
    "start": Game.game_loop,
    "2": show_guide,
    "guide": show_guide,
    "3": quit_game,
    "exit": quit_game,
}

COMMANDS_room = {
    "1": Game.fight,
    "fight": Game.fight,
    "2": Game.avoid,
    "avoid": Game.avoid,
}


def card_selection() -> int:
    option = input("SELECT CARD: ").strip()
    while option not in ["1", "2", "3", "4"]:
        print("ERROR: Invalid Input")
        option = input("SELECT CARD: ")

    return int(option)


def menu_input(commands, state) -> None:
    option = input("SELECT: ").strip().lower()

    while option not in commands:
        print("ERROR: Invalid Input")
        option = input("SELECT: ").strip().lower()

    commands[option](state)
