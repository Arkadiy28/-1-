import re


with open('lesson09_cats_of_ulthar.txt', mode='r') as file:
    fil = file.read().split('\n')
    text = str(fil)

cat = re.findall('кошк[А-я]+', text)

print(len(cat))
