"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    card_value_10 = {'10', 'J', 'Q', 'K'}
    if card in card_value_10:
        value_card = 10
    elif card == 'A':
        value_card = 1
    else:
        value_card = int(card) 

    
    return value_card


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if value_of_card(card_one) < value_of_card(card_two):
        higher = card_two
        return higher
    elif value_of_card(card_one) > value_of_card(card_two):
        higher = card_one
        return higher
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    
    if card_one == "A":
        value_card_1 = 11
    else:
        value_card_1 = value_of_card(card_one)

    if card_two == "A":
        value_card_2 = 11
    else:
        value_card_2 = value_of_card(card_two)

    value_cards = value_card_1 + value_card_2
    
    if value_cards > 10:
        ace_value = 1
    else:
        ace_value = 11
    
    return ace_value


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    card_value_10 = {'10', 'J', 'Q', 'K'}
    if (card_one in card_value_10 or card_two in card_value_10) and (card_one == "A" or card_two == "A"):
        blackjack = True
    else:
        blackjack = False

    print(blackjack)
    return blackjack


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    if value_of_card(card_one) == value_of_card(card_two):
        split_pairs = True
    else:
        split_pairs = False
    return split_pairs


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    if 8 < (value_of_card(card_one)+value_of_card(card_two)) < 12:
        double_down = True
    else:
        double_down = False
    return double_down