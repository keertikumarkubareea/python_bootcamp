"""
The game of blackjack - in Python - Capstone project
"""

import random
import common_constants


def calc_hand_total(hand: dict) -> int:
    """
    Each hand is represented as a dictionary in the following format:
    {card: count}
    For example {TWO: 2, ACE: 1}
    means that the user has 2 cards of TWO and 1 Ace card
    Total = 2 + 2 + 11 = 15
    """
    total = 0
    for card in hand:
        if (card == common_constants.KING_CARD or card == common_constants.QUEEN_CARD or
                card == common_constants.JACK_CARD):
            total += 10 * hand[card]
        elif card == common_constants.ACE_CARD:
            if total > 10:
                total += 1 * hand[card]
            else:
                total += 11 * hand[card]
        else:
            total += int(card) * hand[card]
    return total


def get_card_from_deck(current_deck: dict) -> tuple:
    random_card = random.choice(list(current_deck.keys()))
    # decrement the card count in the deck by 1
    current_deck[random_card] -= 1
    if current_deck[random_card] <= 0:
        current_deck.pop(random_card)
    return random_card, current_deck


def add_card_to_hand(current_hand: dict, card: str) -> dict:
    if card in current_hand:
        current_hand[card] += 1
    else:
        current_hand[card] = 1
    return current_hand


def deal_hands(current_deck: dict, user_hand: dict, dealer_hand: dict) -> tuple:
    # first, we get a card from the current deck to give to the dealer
    card_to_deal, current_deck = get_card_from_deck(current_deck=current_deck)  # current deck has been updated
    # add the card to the dealer's hand
    dealer_hand = add_card_to_hand(current_hand=dealer_hand, card=card_to_deal)
    # second, get a card from the updated deck to give to the user
    card_to_deal, current_deck = get_card_from_deck(current_deck=current_deck)  # current deck updated again
    # add the card to the user's hand
    user_hand = add_card_to_hand(current_hand=user_hand, card=card_to_deal)
    # return the updated deck (2 cards less than the original deck)
    # return the dealer's hand and the user's hand
    return current_deck, user_hand, dealer_hand


def deal_one_hand(current_deck: dict, current_hand: dict) -> tuple:
    """
    This function deals only one hand: either to the user or to the dealer
    :param current_deck: The dictionary containing the most recent deck of available cards
    :param current_hand: The dictionary mapping the cards and their respective counts (user or dealer)
    :return: a tuple (updated deck, updated hand)
    """
    card_to_deal, current_deck = get_card_from_deck(current_deck=current_deck)
    current_hand = add_card_to_hand(current_hand=current_hand, card=card_to_deal)
    return current_deck, current_hand


def main():
    # TODO
    print("Welcome to a game of Blackjack!!")


if __name__ == "__main__":
    main()
