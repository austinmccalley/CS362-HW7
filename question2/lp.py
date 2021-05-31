def leapYear(year):
    if not year.isdigit():
        return False

    year = int(year)

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
