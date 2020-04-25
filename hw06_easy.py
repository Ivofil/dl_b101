# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.

    Исключения:
        - ValueError: вычисление не возможно.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить среднее геометрическое")

def avg_vld():
    """
    Функция, проверки корректности ввода геометрического среднего и его расчета
    """
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = avg(a, b)
        return c
    except ValueError as ex:
        print("Ошибка ввода, повтороите ввод: ", ex)
        return avg_vld()
    except Exception as ex:
        print("Ошибка:", ex)
        return avg_vld()
print(f"Среднее геометрическое = {avg_vld():.2f}")

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

def fld_opr():
    """
    Функция, создающая директории dir_1 - dir_9 в исходной папке
    """
    crt_del = input("\nСоздать(s) или удалить(d) папки?:")
    for i in range(9):
        dir_path = os.path.join(os.getcwd(), "dir_" + str(i + 1))
        if crt_del == "s":
            try:
                os.mkdir(dir_path)
                print(f"Создана папка: {dir_path}") 
            except FileExistsError as es:
                print("Папка уже создана! ")  
        elif crt_del == "d":
            try:
                os.rmdir(dir_path)
                print(f"Удалена папка: {dir_path}") 
            except FileNotFoundError as es:
                print("Папка уже удалена! ") 
        else:
            return fld_opr()
fld_opr()


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


def fld_dir(path):
    """
    Функция, отображающая папки текущей директории
    """
    for fld in os.listdir(path):
        if os.path.isdir(fld):
            print(f"Папка: {fld}, путь: {os.path.abspath(fld)}")
fld_dir(os.getcwd())


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
def copy_mys():
    """
    Функция, создающая копию файла, из которого запущен данный скрипт
    """
    work_file = os.path.realpath(__file__)
    new_file = "Copy_of_" + os.path.basename(work_file)
    shutil.copyfile(work_file, new_file)
    print(f"\nКопия текущего файла {work_file} успешно создана: {new_file}")
copy_mys()
 

 

 
