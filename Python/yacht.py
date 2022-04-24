# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "one"
TWOS = "two"
THREES = "three"
FOURS = "four"
FIVES = "five"
SIXES = "six"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four kind"
LITTLE_STRAIGHT = "little"
BIG_STRAIGHT = "big"
CHOICE = "sum"


def score(dice, category):
    result = 0
    if category == "yacht":
        if dice.count(dice[0]) == 5:
            result = 50
            
    elif category == "one":
        result = dice.count(1)
        
    elif category == "two":
        result = dice.count(2)*2
        
    elif category == "three":
        result = dice.count(3)*3
        
    elif category == "four":
        result = dice.count(4)*4
        
    elif category == "five":
        result = dice.count(5)*5
        
    elif category == "six":
        result = dice.count(6)*6
        
    elif category == "full house":
        count_3 = False
        count_2 = False
        for number in dice:
            if dice.count(number) == 3:
                count_3 = True
            if dice.count(number) == 2:
                count_2 = True
        if count_3 and count_2:
            result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]

    elif category == "four kind":
        for number in dice:
            if dice.count(number) >= 4:
                result = number * 4

    elif category == "little":
        count_1 = False
        count_2 = False
        count_3 = False
        count_4 = False
        count_5 = False
        for number in dice:
            if number == 1:
                count_1 = True
            if number == 2:
                count_2 = True
            if number == 3:
                count_3 = True
            if number == 3:
                count_3 = True
            if number == 4:
                count_4 = True
            if number == 5:
                count_5 = True
        if count_1 and count_2 and count_3 and count_4 and count_5:
            result = 30
                
    elif category == "big":
        count_6 = False
        count_2 = False
        count_3 = False
        count_4 = False
        count_5 = False
        for number in dice:
            if number == 6:
                count_6 = True
            if number == 2:
                count_2 = True
            if number == 3:
                count_3 = True
            if number == 3:
                count_3 = True
            if number == 4:
                count_4 = True
            if number == 5:
                count_5 = True
        if count_6 and count_2 and count_3 and count_4 and count_5:
            result = 30

    elif category == "sum":
        result = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
        
    return result
