def leapYear(year):
    if not year.isdigit():
        return False

    year = int(year)

    if year % 4 == 0:
        return True
