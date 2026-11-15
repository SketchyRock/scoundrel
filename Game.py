from GameState import GameState
from Cards import Card, Suit
import Display
import Handling

def win_condition(state: GameState):
    score = state.HP
    for card in state.room:
        if card.suit == Suit.HEARTS:
            score += card.value
    state.score = score


def lose_condition(state: GameState):
    score = state.HP
    for card in state.main_deck:
        if card.suit == Suit.SPADES or card.suit == Suit.CLUBS:
            score -= card.value
    state.score = score


def equip_weapon(state: GameState, card: Card) -> None:
    state.weapon = card.value
    state.slain = []


def drink_potion(state: GameState, card: Card) -> None:
    if state.can_drink_potion:
        state.HP = min(20, state.HP + card.value)
        state.can_drink_potion = False
    else:
        print("***You can't drink two potions in the same room!***")


def attack_monster(state: GameState, card: Card) -> None:
    if state.weapon == 0:
        state.HP -= card.value
        return

    last_slain = state.slain[-1] if state.slain else None

    if last_slain is not None and card.value >= last_slain:
        state.HP -= card.value
        return

    if state.weapon > card.value:
        state.slain.append(card.value)
    else:
        state.HP -= card.value - state.weapon


def card_action(state: GameState, card: Card) -> None:
    match card.suit:
        case Suit.DIAMONDS:
            equip_weapon(state, card)

        case Suit.HEARTS:
            drink_potion(state, card)

        case Suit.SPADES | Suit.CLUBS:
            attack_monster(state, card)

        case _:
            print("ERROR: card_action() default case")


def fight(state: GameState) -> None:
    state.can_avoid_room = True

    while len(state.room) > 1:
        Display.print_deck_full(state)

        option = Handling.card_selection()

        if 1 <= option <= len(state.room):
            card = state.room[option - 1]
            card_action(state, card)
            state.discard_deck.add_top(card)
            state.room.remove(card)

            if state.HP < 1:
                lose_condition(state)
                return


def avoid(state: GameState):
    if not state.can_avoid_room:
        print("***You can't avoid two rooms in a row!***")
        return

    state.can_avoid_room = False

    for card in state.room:
        state.main_deck.add_bottom(card)

    state.room.clear()
    print("You avoided the room for now...")


def game_loop(state: GameState) -> None:
    state.main_deck.rm_standard_deck()
    state.main_deck.shuffle()
    state.discard_deck.clear()

    while True:
        state.can_drink_potion = True

        if len(state.main_deck) < 4:
            win_condition(state)
            Display.print_result(state)
            return

        while len(state.room) < 4:
            card = state.main_deck.draw_top()
            state.room.append(card)

        Display.print_deck_full(state)
        Display.print_room_menu()
        Handling.menu_input(Handling.COMMANDS_room, state)

        if state.HP < 1:
            Display.print_result(state)
            return
