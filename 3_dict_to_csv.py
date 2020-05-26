"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

data = [
    {'name':'Дмитрий', 'age': 25, 'job': 'Консультант'},
    {'name':'Екатерина', 'age': 32, 'job': 'Аналитик'},
    {'name':'Алексей', 'age': 37, 'job': 'Разработчик'},
    {'name':'X Æ A-Xii', 'age': 1, 'job': 'НЛО'},
]

def main():
    with open('result.csv', 'w', encoding='utf-8', newline='') as f:
        header = ['name', 'age', 'job']
        writer = csv.DictWriter(f, header, delimiter=';')
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    main()
