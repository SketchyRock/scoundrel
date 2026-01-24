from collections import deque
from dataclasses import dataclass
from enum import Enum
import random

# Values assigned to each card rank
RANK_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class Suit(Enum):
    """For readability instead of using only chars for suites"""

    HEARTS = "H"
    DIAMONDS = "D"
    CLUBS = "C"
    SPADES = "S"


@dataclass
class Card:
    """Each Card has a suit, rank, and value of rank"""

    suit: Suit
    rank: str
    value: int


class Deck:
    def __init__(self):
        """initializes the deck with 52 cards,
        one of each rank in each suit"""
        suites = [Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS, Suit.SPADES]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = deque(
            Card(suit=s, rank=r, value=RANK_VALUES[r]) for s in suites for r in ranks
        )

    def clear(self):
        self.cards.clear()

    def rm_standard_deck(self):
        self.cards = deque(
            card
            for card in self.cards
            if not (card.suit in ("H", "D") and card.rank in ("J", "Q", "K", "A"))
        )

    def shuffle(self):
        """casts deque to a list and shuffles,
        deque inefficient for this process without casting"""
        temp = list(self.cards)
        random.shuffle(temp)
        self.cards = deque(temp)

    def draw_top(self) -> Card:
        """removes a card from the top of the deck if exists,
        returns the card drawn"""
        return self.cards.pop() if self.cards else None

    def draw_bottom(self) -> Card:
        """removes a card from the bottom of the deck if exists,
        returns the card drawn"""
        return self.cards.popleft() if self.cards else None

    def add_top(self, card):
        """adds card to top of the deck,
        append()"""
        self.cards.append(card)

    def add_bottom(self, card):
        """adds card to bottom of the deck,
        [0] and push"""
        self.cards.appendleft(card)

    def move_card_to(self, other_deck, from_top=True):
        """moves card from one deck to another,
        either from top or bottom,
        utilizes the draw_top() and draw_bottom() methods"""
        card = self.draw_top() if from_top else self.draw_bottom()

        if card:
            other_deck.add_top(card)

    def __len__(self) -> int:
        """returns the len of Cards in Deck"""
        return len(self.cards)

    def __repr__(self) -> str:
        """returns str of Cards in Deck"""
        return f"Deck({list(self.cards)})"

    def __iter__(self):
        """allows for iteration of each Card in Deck"""
        return iter(self.cards)
