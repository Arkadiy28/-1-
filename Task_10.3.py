shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

fiction = {k:v for k, v in shows.items() if v == 'фантастика'}
print(fiction)

fantasy = {k:v for k, v in shows.items() if v == 'фэнтази'}
print(fantasy)

fiction_list = [k for k, v in fiction.items()]
print(fiction_list)

fantasy_list = [k for k, v in fantasy.items()]
print(fantasy_list)
