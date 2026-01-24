# scoundrel-game
> A classic dungeon-crawler card game implemented in Python.

Scoundrel is a solo card game where you navigate a dungeon using a standard deck of cards. This terminal-based version brings the strategic depth of the physical game to your command line.

---

## Features
* **Dungeon Logic:** Full implementation of Scoundrel rules (Monsters, Weapons, Potions).
* **Terminal Interface:** Play directly in your command line with real-time game state updates.
* **Lightweight:** No heavy dependencies—runs on standard Python 3.

---

## Setup & Installation

### 1. Prerequisites
* Ensure you have **Python 3.8** or higher installed.
* Check your version by running:
  ```bash
  python --version
  ```

### 2. Clone the Project
```bash
git clone [https://github.com/SketchyRock/scoundrel-game.git](https://github.com/SketchyRock/scoundrel-game.git)
cd scoundrel
```

---

## How to Run

### Option A. Standard Execution
```bash
python3 Main.py
```

### Option B. Virtual Environment

```bash
# Create the environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate

# Run the game
python Main.py
```

---

## How to Play
Scoundrel is played with a 52-card deck.

* **Spades & Clubs:** Monsters (Values 2-14, where Jacks=11, Queens=12, Kings=13, Aces=14).
* **Diamonds:** Weapons.
* **Hearts:** Potions.

The goal is to survive the dungeon with as much health as possible by strategically choosing which cards to fight and which to consume.

---

## License

This project is open-source and available under the MIT License.
