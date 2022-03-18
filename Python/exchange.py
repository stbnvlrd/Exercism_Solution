def exchange_money(budget, exchange_rate):
    """
    Estimate value after exchange
    
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    exchanged = float(budget)/float(exchange_rate)
    
    return (exchanged)


def get_change(budget, exchanging_value):
    """
    Calculate currency left after an exchange

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    budget_left = float(budget) - float(exchanging_value)

    return (budget_left)


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate value of bills

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    total_value = denomination * number_of_bills

    return (total_value)


def get_number_of_bills(budget, denomination):
    """
    Calculate number of bills

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    number_bills = budget // denomination
    return(number_bills)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate value after exchange
    
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    new_exchange_rate = float(exchange_rate*(1 + (spread/100)))
    exchanged = int(budget/new_exchange_rate)
    bills_remaining = int (exchanged // denomination)
    maximun_value = denomination * bills_remaining
    return (maximun_value)
    


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    
    new_exchange_rate = float(exchange_rate*(1 + (spread/100)))
    exchanged = int(budget/new_exchange_rate)
    bills_remaining = int (exchanged // denomination)
    maximun_value = exchanged - (denomination * bills_remaining)
    return (maximun_value)
    
    return (bills_remaining)
