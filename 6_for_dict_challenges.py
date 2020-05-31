from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.


students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
c = Counter([name['first_name'] for name in students])
for name in c:
  print(f'{name}: {c.get(name)}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
c = Counter([name['first_name'] for name in students])
result = c.most_common()[0][0]
print(f'Самое частое имя среди учеников: {result}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.

school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
for class_ in school_students:
  class_num = school_students.index(class_) + 1
  c = Counter([name['first_name'] for name in class_])
  result = c.most_common()[0][0]
  print(f'Самое частое имя в классе {class_num}: {result}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.


school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for class_ in school:
  st_list = [name['first_name'] for name in class_['students']]
  boys_girls = ['boy' if is_male.get(name) is True else 'girl' for name in st_list ]
  c = Counter(boys_girls)
  girls_count = c.get('girl', 0)
  boys_count = c.get('boy', 0)
  print(f'В классе {class_["class"]} {girls_count} девочки и {boys_count} мальчика.')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_ in school:
  st_list = [name['first_name'] for name in class_['students']]
  boys_girls = ['boy' if is_male.get(name) is True else 'girl' for name in st_list ]
  c = Counter(boys_girls)
  girls_count = c.get('girl', 0)
  boys_count = c.get('boy', 0)
  class_['girls_count'] = girls_count
  class_['boys_count'] = boys_count

max_girls = max(school, key=lambda x: x['girls_count'])
max_girls_class = max_girls.get('class')

max_boys = max(school, key=lambda x: x['boys_count'])
max_boys_class = max_boys.get('class')

print(f'Больше всего девочек в классе {max_girls_class}')
print(f'Больше всего мальчиков в классе {max_boys_class}')



# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a