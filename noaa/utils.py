from datetime import datetime


def check_date(year, month, day):
    try:
        datetime(int(year), int(month), int(day))
        return True
    except Exception:
        return False
