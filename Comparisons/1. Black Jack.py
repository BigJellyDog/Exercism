"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card in ["J", "K", "Q"]:
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Choosing higher card"""
    card_values = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}

    # Convert numerical cards to integers
    card_one_value = card_values.get(card_one, None)
    card_two_value = card_values.get(card_two, None)

    # Handle the case where the card is not a face card, 'A', or a numerical value
    if card_one_value is None:
        try:
            card_one_value = int(card_one)
        except ValueError as error:
            raise ValueError(f"Invalid card value: {card_one}") from error

    if card_two_value is None:
        try:
            card_two_value = int(card_two)
        except ValueError as error:
            raise ValueError(f"Invalid card value: {card_two}") from error

    # Compare card values
    if card_one_value > card_two_value:
        return card_one
    if card_one_value < card_two_value:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == 1:
        card_one_value = 11
    elif card_two_value == 1:
        card_two_value = 11

    if (card_one_value + card_two_value) + 11 > 21:
        return 1
    return 11


def is_blackjack(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == 1:
        card_one_value = 11
    elif card_two_value == 1:
        card_two_value = 11
    return card_one_value + card_two_value == 21


def can_split_pairs(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    return card_one_value + card_two_value == 20 or card_one_value == card_two_value


def can_double_down(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    return (card_one_value + card_two_value) in [9, 10, 11]
