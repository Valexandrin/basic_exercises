from collections import Counter
from unicodedata import name


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names_all = [students[i]['first_name'] for i in range(len(students))]
names_pepeats = Counter(names_all)
for name in names_pepeats.keys():
    print('{name}: {q_ty}'.format(
        name=name, 
        q_ty=names_pepeats[name]
    ))


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def frequent_name(group):    
    names = [group[i]['first_name'] for i in range(len(group))]    
    names_repeats = Counter(names).most_common()
    return names_repeats[0][0]

print('Most frequent name is {}'.format(frequent_name(students)))


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for ind, cls in enumerate(school_students, start=1):
    print('Most frequent name in class {number}: {name}'.format(
        number=ind, 
        name=frequent_name(cls)
    ))


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for group in school:
    boys = 0
    girls = 0
    for student in group['students']:
        if is_male[student['first_name']]:
            boys += 1 
        else: 
            girls += 1
    print('In class {}: {} girls, {} boys'.format(group['class'], boys, girls))        


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

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

def count_boys(group):
    boys = 0    
    for student in group['students']:
        if is_male[student['first_name']]:
            boys += 1
    return boys

def count_girls(group):
    girls = 0    
    for student in group['students']:
        if not is_male[student['first_name']]:
            girls += 1
    return girls
    

max_boys = (0, 0)
max_girls = (0, 0)
for group in school:    
    boys = count_boys(group)
    girls = count_girls(group)    
    if max_boys[1] < boys:
        max_boys = (group['class'], boys)

    if max_girls[1] < girls:
        max_girls = (group['class'], girls)

print('Most of boys in class {}'.format(max_boys[0]))
print('Most of girls in class {}'.format(max_girls[0]))

'''
for group in school:
    print('Most of {} in class {}'.format(group['gender'], group['class']))
'''