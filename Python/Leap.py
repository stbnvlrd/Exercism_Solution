def leap_year(year):
    if ((year % 4) == 0):
        if ((year % 100) == 0):
            if ((year % 400) == 0):
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False

    return leap_year
