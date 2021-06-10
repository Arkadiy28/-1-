import random, time


def selection_sort(input_list):
    start_time = time.time() # время старта функции
    for i in range(len(input_list)):
        min_i = i
       for j in range(i + 1, len(input_list)):
           if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time # время выполнения в секундах


def standart_sort(input_list):
    start_time = time.time()
    for i in range(len(input_list)):
        input_list.sort()
    return time.time() - start_time



b = [1000, 2000, 5000, 10000]
def unloading(lis, func):
    spisok = []
    for i in lis:
            a = list(range(i))
            spisok.append(i)
            spisok.append(func(a))
    return spisok

print('Функция selection_sort')
print(unloading(b, selection_sort))

print()

print('Функция standart_sort')
print(unloading(b, standart_sort))


# Стандартная функция sort сортирует почти в 2 раза быстрее чем пузырьковая система.
# Потому что пузырковая системе смещает каждый элемент несколько раз пока он не встанет на своё место.
# Стандартаная выбирает елемент и вставляет на своё место.
