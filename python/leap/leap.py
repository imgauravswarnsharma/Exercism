def leap_year(year):
    if not year%4 and year%100:
        return True
    elif not year%100 and not year%400:
        return True
    else:
        return False