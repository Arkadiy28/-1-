def quantity(slovo, fail):
    k = 0
    fails = open(fail)
    a = fails.read()
    b = a.split()
    for i in b:
        if i == slovo:
            k += 1
    print(f'Кол-во повторов слова {slovo}: {k}')

def stroki(slovo, fails):
    with open(fails) as file:
        line = file.readlines()
        for reading in line:
            if slovo in reading:
                print(reading)


fail = open('lesson05_cats_of_ulthar.txt')
print(fail.read())

quantity('кошка', 'lesson05_cats_of_ulthar.txt')

stroki('кошка', 'lesson05_cats_of_ulthar.txt')


fail.close()
