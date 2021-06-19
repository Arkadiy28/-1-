import re


fil = []

with open('lesson09_closest_galaxies.txt', encoding = 'utf-8') as file:
    ee = file.read().split('\n')
    for i in ee:
        fil.append(i.split(','))

qaz = []

for i in fil:
    b = i[0]
    r = i[2]
    w = i[3]
    res = re.search('Андромеда', b)
    rec = re.findall('[0-9].[0-9]{3}', r)
    float_list = [float(x) for x in rec]
    if res and rec:
        asas = dict(Название=b, Расстояние=float_list, Примечания=w)
        qaz.append(asas)

newlist = sorted(qaz, key=lambda k: k['Расстояние'])

print(newlist)
