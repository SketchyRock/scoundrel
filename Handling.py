from sys import exit
import Game

# from GameState import GameState
import Display

COMMANDS_main = {
    "1": Game.game_loop,
    "start": Game.game_loop,
    "2": Display.print_full_guide,
    "guide": Display.print_full_guide,
    "3": exit,
    "exit": exit,
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


def menu_input(commands, state=None):
    option = input("SELECT: ").strip().lower()

    while option not in commands:
        print("ERROR: Invalid Input")
        option = input("SELECT: ").strip().lower()

    while True:
        func = commands.get(option)
        if func:
            if state is not None:
                func(state)
            else:
                func()
            break
        else:
            print("ERROR: function not found")
