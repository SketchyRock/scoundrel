from time import sleep
from GameState import GameState

banner_main_menu = """
  @@@@@@  @@@@@@@  @@@@@@  @@@  @@@ @@@  @@@ @@@@@@@  @@@@@@@  @@@@@@@@ @@@
 !@@     !@@      @@!  @@@ @@!  @@@ @@!@!@@@ @@!  @@@ @@!  @@@ @@!      @@!
  !@@!!  !@!      @!@  !@! @!@  !@! @!@@!!@! @!@  !@! @!@!!@!  @!!!:!   @!!
     !:! :!!      !!:  !!! !!:  !!! !!:  !!! !!:  !!! !!: :!!  !!:      !!:
 ::.: :   :: :: :  : :. :   :.:: :  ::    :  :: :  :   :   : : : :: ::: : ::.: :
        """
line_sep = (
    "==============================================================================="
)
options_main_menu = "1) Start\n2) Guide\n3) Exit"
options_room = "1) Fight\n2) Avoid"

guide_text = """
====================================================
                SCOUNDREL QUICK GUIDE
====================================================

Goal:
  Get through the whole dungeon alive. You start with
  20 HP and can never have more than 20.

----------------------------------------------------
THE DECK
----------------------------------------------------
A standard 52-card deck without the red face cards and
red aces (44 cards). Cards are dealt in rooms of 4.

  Spades, Clubs   Monsters. Damage equals the card value
                  (J=11, Q=12, K=13, A=14).
  Diamonds        Weapons. The value is how much damage
                  the weapon absorbs.
  Hearts          Potions. Restore HP equal to the value.

----------------------------------------------------
EACH ROOM
----------------------------------------------------
1. A room of 4 cards is dealt.
2. FIGHT: resolve 3 of the 4 cards, one at a time, in
   any order. The last card stays for the next room.
   AVOID: put all 4 cards on the bottom of the deck.
   You cannot avoid two rooms in a row.
3. Equipping a weapon replaces the old one. A weapon can
   only be used on a monster weaker than the last one it
   killed. Otherwise you fight bare-handed and take the
   full damage.
4. Only the first potion in a room heals. A second one
   in the same room is wasted.

----------------------------------------------------
THE END
----------------------------------------------------
Clear the dungeon: your score is your HP, plus a potion
left in the final room.
Reach 0 HP: your score is your HP minus the value of
every monster still in the deck.

====================================================
PRESS ENTER TO EXIT
"""


def print_deck_full(state: GameState):
    print("=== ROOM ===")
    for i, card in enumerate(state.room, 1):
        print(f"{i}. {card.rank}{card.suit.value} (val. {card.value})")

    print("--- STATUS ---")
    print(f"HP: {state.HP}")
    print(f"Weapon Damage: {state.weapon}")
    print(f"Enemies Slain: {state.slain}")
    print("--------------")


def print_deck_basic(deck):
    print(line_sep)
    for i, card in enumerate(deck):
        print(f"{i + 1}: {card}")


def print_result(state: GameState):
    print(line_sep)
    if state.HP > 0:
        print(f"You cleared the dungeon with {state.HP} HP. Score: {state.score}")
    else:
        print(f"You died in the dungeon. Score: {state.score}")
    print(line_sep)
    input("Press Enter to return to the menu...")


def print_room_menu():
    print(options_room)


def print_main_menu():
    print(line_sep)
    print(banner_main_menu)
    print(line_sep)
    print(options_main_menu)


def print_full_guide():
    display_text(guide_text)
    input()


def display_text(text):
    for char in text:
        print(char, end="")
        sleep(0.0005)
