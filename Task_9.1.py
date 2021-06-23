import re


def poisk(spicok):
    for i in spicok:
        b = i[0]

        res = re.search('Кит|Рыбы|Пегас', b)
        if res:
            print(res[0], '-' * 10, b)


fil = []

with open('lesson09_closest_galaxies.txt', encoding='utf-8') as file:
    ee = file.read().split('\n')
    for i in ee:
        fil.append(i.split(','))

# Выдаёт все латинские названия
for i in fil:
    b = i[0]
    res = re.match('[A-z]+', b)
    if res:
        print(b)

# Выдает названия которые заканчиваются на цифры
for i in fil:
    b = i[0]
    res = re.findall('\s[0-9]+$', b)
    if res:
        print(b)

# Выборка Кит, Рыбы, Пегас
poisk(fil)
