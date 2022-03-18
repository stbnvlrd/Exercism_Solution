def eat_ghost(power_pellet_active, touching_ghost):
    """

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if power_pellet_active == True and touching_ghost == True:
        eating_ghost = True
    else:
        eating_ghost = False
    return eating_ghost


def score(touching_power_pellet, touching_dot):
    """

    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    if touching_power_pellet == True or touching_dot == True:
        scoring = True
    else:
        scoring = False
    return scoring


def lose(power_pellet_active, touching_ghost):
    """

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    if power_pellet_active == True or (power_pellet_active == False and touching_ghost == False):
        pac_man_loses = False
    else:
        pac_man_loses = True
    return pac_man_loses


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if power_pellet_active == True or (power_pellet_active == False and touching_ghost == False):
        pac_man_loses = False
    else:
        pac_man_loses = True
    if pac_man_loses == False and has_eaten_all_dots == True:
        pac_man_wins = True
    else:
        pac_man_wins = False
    return pac_man_wins
