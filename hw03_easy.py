# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
N = 0
for FRT in fruits:
    N += 1
    print(f'{N}. {FRT:>6}')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

sp1 = [1, 2, 3, 1, 1, 2, 3, 0, 2, 0, 'abc', 'dfs']
sp2 = [1, 2, 0, 'dfs']
for i2 in sp2:
    for i1 in sp1[:]:
        if i1 == i2:
            sp1.remove(i1)
print(sp1)        
print(sp2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

sps1 = [1, 2, 3, 1, 1, 2, 3, 0, 2, 0, 20, 101, 200]
sps2 = []
for elm in sps1:
    if elm % 2 ==0:
        sps2.append(elm / 4)
    else:
        sps2.append(elm * 2)
print(sps1)
print(sps2)

