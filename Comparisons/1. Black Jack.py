"""Functions to help play and score a game of blackjack."""


def value_of_card(card):
    if card == "J" or card == "Q" or card == "K":
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    if card_one == card_two:
        return card_one, card_two
    elif card_one in ["10", "J", "Q", "K"] and card_two == 10:
        return card_one, card_two
    elif card_two in ["10", "J", "Q", "K"] and card_one == 10:
        return card_two, card_one
    elif card_one not in ["A", "10", "J", "Q", "K"] or card_two not in ["A", "10", "J", "Q", "K"]:
        bigger_value = max(int(card_one), int(card_two))
        return str(bigger_value)
    elif card_one in ["J", "Q", "K", "10"] and card_two not in ["J", "Q", "K", "10"]:
        return card_one
    else:
        return card_two


print(higher_card("K", "K"))


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass
