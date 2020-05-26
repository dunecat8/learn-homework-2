"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, timedelta, datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru-RU')

def print_days():
    yesterday = (date.today() - timedelta(days=1)).strftime('%d %B %Y')
    today = date.today().strftime('%d %B %Y')
    thirty_days_ago = (date.today() - timedelta(days=30)).strftime('%d %B %Y')

    print(f'Вчера было {yesterday}')
    print(f'Сегодня {today}')
    print(f'30 дней назад было {thirty_days_ago}')

def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
