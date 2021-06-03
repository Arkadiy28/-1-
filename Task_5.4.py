# Дневник

data = input('Введите дату: ')
event = input('Раскажите о событии: ')


with open('diary.txt', mode='a+') as saplain:
    saplain.write(f'Сегодня {data}, {event} \n')


with open('diary.txt', mode='r') as sapl:
    print(sapl.read())
