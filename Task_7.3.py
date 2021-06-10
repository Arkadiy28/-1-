import random, time



def selection_sort(input_list):
    start_time = time.time() # время старта функции
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]: min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time # время выполнения в секундах


f = []
b = [1000, 2000, 5000, 10000]
for i in b:
        a = list(range(i))
        f.append(i)
        f.append(selection_sort(a))

print(f)
