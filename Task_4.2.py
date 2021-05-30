anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

olya_crossing = set(anya).intersection(set(olya))

nastya_crossing = set(anya).intersection(set(nastya))

sveta_crossing = set(anya).intersection(set(sveta))

while True:
    if olya_crossing > nastya_crossing and olya_crossing > sveta_crossing:
        print('У Ани больше всего общих любимых сериалов с Олей')
    elif nastya_crossing > olya_crossing and nastya_crossing > sveta_crossing:
        print('У Ани больше всего общих любимых сериалов с Настей')
    else:
        print('У Ани больше всего общих любимых сериалов со Светой')
    break
