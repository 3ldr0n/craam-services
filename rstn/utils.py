from datetime import datetime


def check_date(year, month, day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        datetime(year, month, day)
        return True
    except ValueError:
        return False
