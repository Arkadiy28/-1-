import numpy
import pickle


shows = {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, 'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
         'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'}, '24': {'Genre': 'драма', 'Rating': 0.75},
         'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98},
         'Во все тяжкие': {'Жанр': 'криминал', 'Рейтинг': '0.85'},
         'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87}, 'Карточный домик': {'Genre': 'драма', 'Rating': 0.82},
         'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}}


def fukciya(zhanr):
    ratings = []
    serials = []
    films = {}
    for k, v in shows.items():
        if v.get('Жанр') == zhanr:
            ratings.append(float(v.get('Рейтинг')))
            films.setdefault(k)
        elif v.get('Genre') == zhanr:
            ratings.append(float(v.get('Rating')))

        for t, l in v.items():
            if l == zhanr:
                serials.append(t)
    serial = len(serials)
    rating = round(((sum(ratings)) / (len(ratings))), 2)
    print(f'Число сериалов {serial}, средний рейтинг {rating}')
    with open(f'{zhanr}.dat', mode='wb') as saplain:
        pickle.dump(f'{films}', saplain)


def zanry():
    zhanr = []
    for k, v in shows.items():
        for t, l in v.items():
            if t == 'Жанр':
                zhanr.append(l)
            elif t == 'Genre':
                zhanr.append(l)
    return (set(zhanr))




for i in zanry():
    fukciya(i)
