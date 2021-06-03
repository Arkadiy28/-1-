def quantity(slovo, fails):
    fail = open(fails)
    a = fail.read()
    print(a.count(slovo))

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
