# scoundrel

A terminal version of Scoundrel, the solo dungeon-crawling card game played with a standard deck of cards. You start with 20 HP, fight through the deck room by room, and try to get out alive.

## Running it

You need Python 3.10 or newer. There are no dependencies.

```bash
git clone https://github.com/SketchyRock/scoundrel.git
cd scoundrel
python3 Main.py
```

The main menu has three options: start a game, read the in-game guide, or exit.

## How to play

The deck is a standard 52-card deck without the red face cards and red aces, which leaves 44 cards. They are dealt in rooms of four.

| Cards | Role | Effect |
|---|---|---|
| Spades and clubs | Monsters | Damage equal to the card value (J=11, Q=12, K=13, A=14) |
| Diamonds | Weapons | The value is how much damage the weapon absorbs |
| Hearts | Potions | Restore HP equal to the value, up to 20 |

In each room you either fight or avoid.

- **Fight.** Resolve three of the four cards, one at a time and in any order. The last card stays for the next room.
- **Avoid.** Put all four cards on the bottom of the deck. You can't avoid two rooms in a row.
- **Weapons.** Equipping one replaces the old weapon. It can only be used on a monster weaker than the last one it killed. Otherwise you take the full damage.
- **Potions.** Only the first potion in a room heals. A second one in the same room is wasted.

If you clear the dungeon, your score is your HP plus a potion left in the final room. If you reach 0 HP, your score is your HP minus the value of every monster still in the deck.

## Project layout

| File | Purpose |
|---|---|
| `Main.py` | Entry point and main menu loop |
| `Game.py` | Game rules: fighting, avoiding, weapons, potions, scoring |
| `Cards.py` | `Card`, `Suit`, and `Deck` |
| `GameState.py` | HP, weapon, room, and decks for one run |
| `Handling.py` | Input handling and menu commands |
| `Display.py` | Menus, the room display, and the in-game guide |

## Roadmap

- Track wins, losses, and monsters slain across runs, saved to a file
- A stats screen
- Risk your score from a run for a bigger reward on the next one
- A classic mode, and a roguelite mode where score is currency

## License

MIT. See [LICENSE](LICENSE).
