# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
for person in students:
    names.append(person["first_name"])
names_count = Counter(names)
for name, count in names_count.items():
    print('{name}: {count}'.format(name = name, count = count))



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

def most_freq(students: list):
    names = []
    for person in students:
        names.append(person["first_name"])
    most_freq_name = Counter(names).most_common(1)
    return most_freq_name[0][0]
name = most_freq(students)
print('Самое частое имя среди учеников: {name}'.format(name = name))

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
for idx, classes in enumerate(school_students, start=1):
    name = most_freq(classes)
    print('Самое частое имя в классе {num_class}: {name}'.format(num_class = idx, name = name))


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
def get_gender(name, genders):
    return 'мужской' if genders[name] else 'женский'


def nums_girls_boys(school: list, genders):
    count_genders = []
    for classes in school:
        boys_and_girls = {'class': classes['class'], 'boys': 0, 'girls': 0}
        for student in classes['students']:
            gender = get_gender(student['first_name'], genders)
            if gender == 'мужской':
                boys_and_girls['boys'] += 1
            else:
                boys_and_girls['girls'] += 1
        count_genders.append(boys_and_girls) 
    return count_genders

for class_name in nums_girls_boys(school, is_male):
    cl = class_name['class']
    boys = class_name['boys']
    girls = class_name['girls']
    print('Класс {cl}: девочки {gl}, мальчики {bs}'.format(cl = cl, gl = girls, bs = boys))



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
max_boys, max_girls = 0, 0
max_b_g = {'max_b': '', 'max_girls': 0}

children = nums_girls_boys(school, is_male)
for classes in children:
    boys = classes['boys']
    girls = classes['girls']
    if  boys > max_boys:
        max_boys = boys
        max_b_g['max_b'] = classes['class']
    if girls > max_girls:
        max_girls = girls
        max_b_g['max_g'] = classes['class']
    
print(f'Больше всего мальчиков в классе {max_b_g["max_b"]}')
print(f'Больше всего девочек в классе {max_b_g["max_g"]}')



