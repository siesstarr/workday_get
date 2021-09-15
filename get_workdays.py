from datetime import date, timedelta
from pprint import pprint

year = 2021
workdays = {}
not_work = {
    1: [1, 2, 3],
    2: [11, 12, 13, 14, 15, 16, 17],
    4: [3, 4, 5],
    5: [1, 2, 3, 4, 5],
    6: [12, 13, 14],
    9: [19, 20, 21],
    10: [1, 2, 3, 4, 5, 6, 7],
}
need_work = {
    2: [7, 20],
    4: [25],
    5: [8],
    9: [18, 26],
    10: [9],
}
day = date(year=year, month=1, day=1)

while True:
    if day.month not in workdays:
        workdays[day.month] = {
            'need_work': [],
            'not_work': [],
            'need_work_days': 0,
        }
    if day.isoweekday() in [
            1, 2, 3, 4, 5
    ] and not (day.month in not_work and day.day in not_work[day.month]):
        workdays[day.month]['need_work'].append(day.isoformat())
        workdays[day.month]['need_work_days'] = workdays[
            day.month]['need_work_days'] + 1
    elif day.month in need_work and day.day in need_work[day.month]:
        workdays[day.month]['need_work'].append(day.isoformat())
        workdays[day.month]['need_work_days'] = workdays[
            day.month]['need_work_days'] + 1
    day = day + timedelta(days=1)
    if day.year != year:
        break

pprint(workdays)
