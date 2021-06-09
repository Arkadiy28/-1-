a = [19, 2, 31, 45, 6, 11, 121, 27]


def sort(list):
    for spisok in range(len(list)-1, 0, -1):
        for i in range(spisok):
            if list[i] < list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    print(list)


sort(a)
