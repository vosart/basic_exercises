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
names_list = []
for person in students:
    names_list.append(person["first_name"])
names_count = Counter(names_list)
for name, count in names_count.items():
    print(f'{name}: {count}')

# или вариант без Counter
#
# names_list = {}
# for student in students:
#     name = student['first_name']
#     if  name in names_list:
#         names_list[name] += 1
#     else:
#         names_list[name] = 1
# for name, count in names_list.items():
#     print(f'{name}: {count}')



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
    names_list = []
    for person in students:
        names_list.append(person["first_name"])
    most_freq_name = Counter(names_list).most_common(1)
    return most_freq_name[0][0]
name = most_freq(students)
print(f'Самое частое имя среди учеников: {name}')

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
list_of_freq_names = []
num_class = 1
for classes in school_students:
    name = most_freq(classes)
    print(f'Самое частое имя в классе {num_class}: {name}')
    num_class += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2
from for_challenges import genders # импорт из предыдущего задания
    
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

def nums_girls_boys(school: list, list_genders):
    list_classes = []
    for classes in school:
        boys_and_girls = {'class': classes['class'], 'boys': 0, 'girls': 0}
        for student in classes['students']:
            gender = genders(student['first_name'], list_genders)
            if gender == 'мужской':
                boys_and_girls['boys'] += 1
            else:
                boys_and_girls['girls'] += 1
        list_classes.append(boys_and_girls) 
    return list_classes

for class_name in nums_girls_boys(school, is_male):
    cl = class_name['class']
    boys = class_name['boys']
    girls = class_name['girls']
    print(f'Класс {cl}: девочки {girls}, мальчики {boys}')



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
print(nums_girls_boys(school, is_male))


