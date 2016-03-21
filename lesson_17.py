# coding: utf-8
import sqlite3

# открываем или создаем базу
conn = sqlite3.connect('example.db')

# создаем курсор - точка доступа к таблице БД
c = conn.cursor()

try:
    # создаем таблицу
    c.execute('CREATE TABLE students (name text, date text)')

    # сохраняет изменения в БД
    conn.commit()

except sqlite3.OperationalError:
    pass



# закрываем соединение
conn.close()



