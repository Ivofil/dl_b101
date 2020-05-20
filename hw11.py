"""
Реализовать решение следующей задачи: 
«Есть два писателя, которые по очереди в течении определенного 
времени (у каждого разное) пишут в одну книгу. Данная книга очень 
популярна, у неё есть как минимум 3 фаната (читателя), которые 
ждут не дождутся, чтобы прочитать новые записи из неё. Каждый 
читатель и писатель – отдельный поток. Одновременно книгу может 
читать несколько читателей, но писать единовременно может 
только один писатель.»
"""

from threading import Thread, Lock, currentThread
from random import random, randint
import time


txt_dict = "Пять безмолвных философов сидят вокруг круглого стола перед каждым".split(" ")
book = ["", 10, 0]
mutex = Lock()

def writer():
    global book
    while book[2] < book[1]:
        mutex.acquire()
        book[2] += 1
        book[0] += f"{txt_dict[randint(1,len(txt_dict))-1]} "
        print(f"\nПисатель {currentThread().getName()}, написал {book[2]} главу книги: \n{book[0]}")
        mutex.release()
        time.sleep(random())
    print(f"\nВеликолено! Писатель {currentThread().getName()}, завершил написание романа")
  
def reader():
    global book
    while book[2] < book[1]:
        print(f"\nЧитатель {currentThread().getName()}, прочел очередную главу книги: \n{book[0]}")
        time.sleep(random())
    print(f"\nВеликолено! Читатель {currentThread().getName()}, прочел полностью книгу!")

def book_run(num_readers=3, num_glav=10):
    book[1] = num_glav
    threads_book = (Thread(target=writer) if i < 2 else Thread(target=reader) for i in range(num_readers+2))
    for t in threads_book:
        t.start()
    for t in threads_book:    
        t.join()


if __name__ == '__main__':
    book_run()
