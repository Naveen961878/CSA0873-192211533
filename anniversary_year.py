def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
def find_anniversary_date(date):
    day, month, year = map(int, date.split('/'))
    if is_leap_year(year):
        print(f"Given Anniversary Year: Leap Year. Next Anniversary Date: {day}/{month}/{year + 1}")
    else:
        print(f"Given Anniversary Year: Non Leap Year. Previous Anniversary Date: {day}/{month}/{year - 1}")
date = input("enter anniversary date")
find_anniversary_date(date)
