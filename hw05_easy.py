# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
def sqr_lst(lst):
    """
    Создание нового списка со значениями квадратов исходного
    """
    lst_s = [i**2 for i in lst]
    print(f"{lst} > {lst_s}")
sps1 = [random.randint(0,10) for i in range(10)]
sqr_lst(sps1)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fr_lst1 = ["яблоко", "персик", "груша", "манго", "абрикос"]
fr_lst2 = ["виноград", "персик", "манго"]
print(list(set(fr_lst1 + fr_lst2)))
print(list(set(fr_lst1).union(set(fr_lst2))))


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst_new = [random.randint(-100,100) for i in range(20)]
lst_krt = [i for i in lst_new if i % 3 == 0 and i > 0 and i % 4 != 0]
print(f"{lst_new} > {lst_krt}")
