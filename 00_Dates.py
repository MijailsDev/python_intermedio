### Dates ###

from datetime import datetime

now = datetime.now()        # Va a inicializar un onbjeto de tipo datetime

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)


year_2023 = datetime(2023, 1, 1)

print(year_2023)
