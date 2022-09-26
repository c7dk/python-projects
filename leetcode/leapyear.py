year = int(input("Please input the year: "))
month = int(input("Please input the month: "))


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if leap_year(year):
            print(29)
        else:
            print(28)
    else:
        print(days[month - 1])


days_in_month(year, month)
