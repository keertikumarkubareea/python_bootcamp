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
    print("----------------------------------------------------")
    ready_to_play = ""
    while ready_to_play.lower() != "yes":
        ready_to_play = input("Is the player ready to play? ('yes'/'no'): ")
    deck = common_constants.START_DECK
    print("The deck of cards has been shuffled . . .")
    player = {}
    dealer = {}
    deck, player, dealer = deal_hands(current_deck=deck, user_hand=player, dealer_hand=dealer)
    initial_dealer_score = calc_hand_total(hand=dealer)
    player_score = calc_hand_total(hand=player)
    print("Show of first card:")
    print(f"The dealer has the following cards {dealer} with the following score: {initial_dealer_score}")
    print(f"The player has the following cards {player} with the following score: {player_score}")
    print("The first hands have been distributed and revealed.")
    print("---------------------------------------------------")
    dealer_score = initial_dealer_score
    game_on = True
    while game_on:
        print(f"Your score is {player_score}")
        player_draw = ""
        while player_draw != "yes" and player_draw != "no":
            print("Please enter 'yes' or 'no'. . .")
            player_draw = input("Would you like to draw a card from the deck? ('HIT'): ")
        if player_draw == "no":
            print("Player chose to STAND and not take a card")
            game_on = False
        else:
            deck, player = deal_one_hand(current_deck=deck, current_hand=player)
            player_score = calc_hand_total(hand=player)
            print(f"Player has the following hand: {player}")
            print(f"Player has the following score: {player_score}")
            if player_score > 21:
                # Player Bust - will be printed outside the loop
                game_on = False
                # Immediate loss of Player - break out of the loop
                continue
        if dealer_score < 21:
            deck, dealer = deal_one_hand(current_deck=deck, current_hand=dealer)
            dealer_score = calc_hand_total(dealer)
            print(f"Dealer has acquired a card (hidden)")
            # calculating the number of cards that the dealer has
            dealer_cards = 0
            for card in dealer:
                dealer_cards += dealer[card]
            print(f"Dealer has the score of {initial_dealer_score} + the score from {dealer_cards - 1} more cards")
            if dealer_score > 21:
                # Dealer Bust - will be printed outside the loop
                game_on = False
                # Immediate loss of Dealer - break out of the loop
                continue

    print("----------------------------------------------------")
    print(f"Dealer hand: {dealer}")
    print(f"Dealer score: {dealer_score}")
    print("----------------------------------------------------")
    print(f"Player hand: {player}")
    print(f"Player score: {player_score}")
    if dealer_score > 21:
        print("Dealer BUSTED")
        print("Player wins!!")
    elif player_score > 21:
        print("Player BUSTED")
        print("Dealer wins!!")
    # No one is busted from here on
    elif player_score == dealer_score:
        print("DRAW")
    elif player_score > dealer_score:
        print(f"Player wins with a score of {player_score}")
        print(f"Dealer loses with {dealer_score} points")
    else:
        print(f"Dealer wins with a score of {dealer_score}")
        print(f"Player loses with {player_score} points")


if __name__ == "__main__":
    main()
