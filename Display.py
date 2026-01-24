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
  Survive the Dungeon and finish with the highest HP.
  You start with 20 HP and face 4-card “Rooms.”

----------------------------------------------------
HOW TO PLAY
----------------------------------------------------
1. Draw a Room:
   - Reveal 4 cards from the Dungeon deck.

2. Choose to FIGHT or AVOID:
   - FIGHT: Battle each card in the room one at a time.
   - AVOID: Skip the room by placing all 4 cards at the
     bottom of the deck.
     *** You cannot avoid two rooms in a row! ***

3. Fighting Cards:
   - Monsters (2-10): Deal damage equal to their value.
   - Weapons (J, Q, K): Equip them to fight stronger foes.
   - Aces (A): Restore HP (heal amount depends on rules).
   - Others: Handle by your game's custom rules.

4. End of Dungeon:
   - If you clear the deck → your HP is your final score.
   - If HP drops to 0 → remaining monster values become
     your negative score.

----------------------------------------------------
CARD REFERENCE
----------------------------------------------------
  Card Type   | Effect
  --------------------------------------------
  2-10        | Monster (damage = value)
  J           | Weapon (damage = 11)
  Q           | Weapon (damage = 12)
  K           | Weapon (damage = 13)
  A           | Heal / Potion
  ♥ ♦ (Red)   | Often healing or safe cards
  ♣ ♠ (Black) | Often weapons or monsters

----------------------------------------------------
TURN SUMMARY
----------------------------------------------------
1. Draw a new room (4 cards)
2. Choose: FIGHT or AVOID
3. Resolve the cards
4. Manage HP and weapon
5. Continue until deck empty or HP ≤ 0

====================================================
        Survive, adapt, and escape the dungeon.
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
