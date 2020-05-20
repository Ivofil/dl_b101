"""
Пять безмолвных философов сидят вокруг круглого стола, 
перед каждым философом стоит тарелка спагетти. Вилки лежат 
на столе между каждой парой ближайших философов. Каждый 
философ может либо есть, либо размышлять. Прием пищи не 
ограничен количеством оставшихся спагетти — 
подразумевается бесконечный запас. Тем не менее, философ 
может есть только тогда, когда держит две вилки — взятую 
справа и слева (альтернативная формулировка проблемы 
подразумевает миски с рисом и палочки для еды вместо 
тарелок со спагетти и вилок). Каждый философ может взять 
ближайшую вилку (если она доступна) или положить — если он 
уже держит её. Взятие каждой вилки и возвращение её на стол 
являются раздельными действиями, которые должны 
выполняться одно за другим. Вопрос задачи заключается в том, 
чтобы разработать модель поведения (параллельный 
алгоритм), при котором ни один из философов не будет 
голодать, то есть будет вечно чередовать приём пищи и 
размышления
"""

from threading import Thread, Lock, currentThread
from random import random, randint
import time

vilki = []
phil_list = []
phil_num_dinners = []
phil_var = ["Кафка", "Платон", "Сократ", "Кант", "Локк", "Экстрафилософ)"]
mutex = Lock()

def check_vilki(thread_num):
    """Функция определяющая есть ли обе вилки в руках философа"""
    global vilki, phil_num_dinners
    #print(f"\nПроверка {phil_list[thread_num]} {vilki}: {vilki[thread_num-1]} {vilki[thread_num]}") 
    if vilki[thread_num-1] == thread_num and vilki[thread_num] == thread_num:
        phil_num_dinners[thread_num] += 1
        print(f"Философ {phil_list[thread_num]} поел {phil_num_dinners[thread_num]} раз, время размышлять!")
        #print(f"{phil_num_dinners}\n")
        vilki[thread_num-1], vilki[thread_num] = "", ""
        time.sleep(random())
        
def try_vilki(thread_num):
    """Функция работы со случайной вилкой(левой или правой)"""
    global vilki
    num_vilki = randint(thread_num-1, thread_num)
    if num_vilki < 0:
        num_vilki = len(vilki) - 1  
    mutex.acquire()
    print(f"{phil_list[thread_num]} пробует взять вилку {num_vilki} ")
    if vilki[num_vilki] == "":
        vilki[num_vilki] = thread_num
        print(f"{phil_list[thread_num]}, успешно взял вилку #{num_vilki}: {vilki}")
    elif vilki[num_vilki] == thread_num:
        vilki[num_vilki] = ""
        print(f"{phil_list[thread_num]}, положил обратно вилку #{num_vilki} на стол:  {vilki}")
    else:
        print(f"Вилка #{num_vilki} уже занята {phil_list[vilki[num_vilki]]}: {vilki}")
    mutex.release()
    time.sleep(random())
    

def phi(num):
    global vilki, phil_num_dinners
    print(f"\n{phil_list[num]} сел за стол под номером #{num}")
    while phil_num_dinners[num] < 5:
        #print(f"{phil_list[num]} {phil_num_dinners[num]}")
        if phil_num_dinners[num] > min(phil_num_dinners) + 1:
            print(f"\n---{phil_list[num]} подожду голодных: {phil_num_dinners}")
            time.sleep(random())
        else:
            try_vilki(num)
            check_vilki(num)
    print(f"\nОТЛИЧНО! {phil_list[num]} завершил философский обед {phil_num_dinners}\n")
            

def philosoph_dinner(num_phi=2):
    global vilki, phil_list, phil_num_dinners
    phil_num_dinners = [0 for _ in range(num_phi)]
    phil_list = [(phil_var[_ if _ < 5 else 5]) for _ in range(num_phi)]
    vilki = ["" for _ in range(num_phi)]
    threads_phi = (Thread(target=phi, args=(_,)) for _ in range(num_phi))
    for t in threads_phi:
        t.start()
    for t in threads_phi:    
        t.join()


if __name__ == '__main__':
    philosoph_dinner(5)
