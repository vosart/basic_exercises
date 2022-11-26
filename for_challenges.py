# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
print(*names, sep='\n')


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print('{name}: {liters}'.format(name = name, liters = len(name)))


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша'] # зачем тут это, не понял

# Сделал функцию, чтобы использовать в след задаче

def genders(names, list_genders):
    if list_genders[names] is True:
            return 'мужской'
    return 'женский'
for name in names:
    gender = genders(name, is_male)
    print(f'{name}: {gender}')

# Задание 4
# Даны группы учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
print('Всего {num_groups} группы.'.format(num_groups = len(groups)))
group_number = 1
for group in groups:
    group_length = len(group)
    print(f'Группа {group_number}: {group_length} ученика.')
    group_number += 1


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
group = 1
for students in groups:
    print(f'Группа {group}: ', end='')
    print(*students, sep=', ')   
    group += 1