"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    next_round = [number, number+1, number+2]
    return next_round


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    average = sum(hand)/len(hand)
    return average
    


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    average = sum(hand)/len(hand)
    average_1 = (hand[0] + hand[-1])/2
    largo = (int(len(hand)) - 1 ) // 2
    average_2 = hand[largo]
    if average_1 == average or average_2 == average:
        result = True
    else:
        result = False
    print(result)
    return result


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    largo = len(hand)
    x = 0
    count_even = 0
    count_odd = 0
    even = 0
    odd = 0
    while x < largo:
        if (x % 2) == 0:
            even = even + hand[x]
            count_even = count_even + 1
        else:
            odd = odd + hand[x]
            count_odd = count_odd + 1
        x = x + 1
    if (even/count_even) == (odd/count_odd):
        result = True
    else:
        result = False
    print(result)
    return result


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    result = [hand[0],hand[1]]
    if hand[-1] == 11:
        result.append(22)
    else:
        result.append(hand[-1])
    return result
