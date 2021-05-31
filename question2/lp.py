def leapYear(year):
    if not year.isdigit():
        return False

    year = int(year)

    if year % 4 == 0:
        if year % 100 == 0:
            return False
        return True
