# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import re
info_w = []
info_h = []
info =[]

workers = open('data/workers.txt', 'r', encoding='utf-8')
for line in workers:
    #print(line)
    info_w.append(re.findall(r'[А-я]+[_]?[А-я]+|[0-9]+', line))
workers.close()

hours = open('data/hours_of.txt', 'r', encoding='utf-8')
for line in hours:
    #print(line)
    info_h.append(re.findall(r'[А-я]+\s?[А-я]+|[0-9]+', line))
hours.close()

#print(info_w)
#print(info_h)

zp = open('data/zp.txt', 'w', encoding='utf-8')
zp.write('Имя Фамилия Заработанная плата\n')
info_w = info_w[1:]
info_h = info_h[1:]

for i in info_w:
    name_one_table = i[0]
    surname_one_table = i[1]
    for n in info_h:
        name_two_table = n[0]
        surname_two_table = n[1]
        if name_one_table == name_two_table and \
            surname_one_table == surname_two_table:
            ok = int(i[2])      
            nt = int(i[4])  
            wt = int(n[2])  
            work = wt - nt
            if work > 0:
                price = ok + 2 * ok * (wt / nt - 1)
            else:
                price = ok * wt / nt
            
            person_data = f'{name_one_table} {surname_one_table} {price:.2f}\n'
            print(person_data)
            zp.write(person_data)
zp.close()


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


def write_in_file(name, lst):
    """
    Функция, распределения элементов по алфавиту
    """
    file_name = 'data/fruits_' + name + '.txt'
    file = open(file_name, 'w', encoding='utf-8')
    for n in lst:
        file.write(n)
    file.close()

alf = list(map(chr, range(ord('А'), ord('Я')+1)))

for sim in alf:
    fruits = open('data/fruits.txt', 'r', encoding='utf-8')
    #print(sim, '---------------->')
    alf_lst = []
    for line in fruits:
        if line[0] == sim:
            #print(sim, '>', line)
            alf_lst.append(line)
    if alf_lst != []:
        write_in_file(sim, alf_lst)


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


equation = '-7/11 - -5 4/5'
equation2 = '-1/9 + 1/3'
params = re.findall(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
funcs = re.split(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
print(equation, params, funcs[1])
#Далее слишком запутанная функция вышла(
