# 1. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
my_list = [2, 4, 8, 9, 3, 81, 4, 11, 2, 8]

def get_unic(my_list):
    unic = []
    for i in range(len(my_list)):
        if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
            unic.append(my_list[i])
    return unic

print(get_unic(my_list))

