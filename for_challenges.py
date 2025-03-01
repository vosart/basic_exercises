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

def get_gender(name):
    return 'мужской' if is_male[name] else 'женский'
for name in names:
    gender = get_gender(name)
    print(f'{name}: {gender}')


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
for idx, group in enumerate(groups, start=1):
    print('Группа {num}: {amount} ученика'.format(num = idx, amount = len(group)))



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

for idx, group in enumerate(groups, start=1):
    print('Группа {num}: '.format(num = idx), end='')
    print(*group, sep=', ')  