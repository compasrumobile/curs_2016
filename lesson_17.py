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

    print('create students...')

except sqlite3.OperationalError:
    pass


try:
    # создаем таблицу
    c.execute('CREATE TABLE books (name text, date text)')

    # сохраняет изменения в БД
    conn.commit()

    print('create books...')

except sqlite3.OperationalError:
    pass


# закрываем соединение
conn.close()



