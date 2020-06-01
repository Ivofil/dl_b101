"""
Реализовать структуру базы и запросы из предыдущего дз с использованием 
Python DB-API.
"""
import sqlite3

def dbi_execute(ask):
    print("\n")
    for row in cursor.execute(ask):
        print(*row)    
#conn = sqlite3.connect('Chinook_Sqlite.sqlite')
conn = sqlite3.connect("DL.db")
cursor = conn.cursor()
#cursor.execute("INSERT INTO sportsman VALUES(10001, \"Нововов Иван\", \"КМС\", 1990, 10, \"Россия\");")
conn.commit()

dbi_execute("SELECT * FROM sportsman")
dbi_execute("SELECT competition_name, world_record FROM competition")
dbi_execute("SELECT sportsman_name, year_of_birth  FROM sportsman WHERE year_of_birth = 1990")
dbi_execute("SELECT city FROM result WHERE hold_date = \"12-05-2010\" OR hold_date = \"15-05-2010\"")
dbi_execute("SELECT hold_date FROM result WHERE city = \"Москва\" AND result = 10")
dbi_execute("SELECT sportsman_name FROM sportsman WHERE personal_record < 25")        
conn.close()
