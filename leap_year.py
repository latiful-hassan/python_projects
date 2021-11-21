
def is_year_leap(year):
    if test_years[i] % 4 == 0:
        if test_years[i] % 100 == 0:
            if test_years[i] % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        if month == 2:
            return 29
    return month_days[month - 1]

def day_of_year(year, month, day):
    if year < 1582:
        return None
    if month > 12 or month < 1:
        return None
    if day > 31 or day < 1:
        return None

    totaldays = day
    month = month - 1
    while month > 0:
        totaldays += days_in_month(year, month)
        month -= 1

    return totaldays


print(day_of_year(2000, 12, 31))

