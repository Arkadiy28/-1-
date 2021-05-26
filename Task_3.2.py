print('Полная таблица умножения')

for i in range(1, 10):
    for k in range(1, 11):
        print(f'{i} * {k} = {i * k}\t', end='\n')
    print('')
else:
    print('End off')
