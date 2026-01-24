from Cards import Deck

class GameState:
    def __init__(self):
        self.main_deck = Deck()
        self.discard_deck = Deck()
        self.HP = 20
        self.weapon = 0
        self.slain = []
        self.room = []
        self.can_avoid_room = True
        self.can_drink_potion = True
        self.score = None
