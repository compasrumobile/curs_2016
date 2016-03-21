# coding: utf-8
import sqlite3

# открываем или создаем базу
conn = sqlite3.connect('example.db')

# создаем курсор - точка доступа к таблице БД
c = conn.cursor()

try:
    # создаем таблицу
    c.execute('CREATE TABLE students (id INTEGER, name text, date text)')

    # сохраняет изменения в БД
    conn.commit()

    print('create students...')

except sqlite3.OperationalError:
    pass


try:
    # создаем таблицу
    c.execute('CREATE TABLE books (id INTEGER, name text, date text)')

    # сохраняет изменения в БД
    conn.commit()

    print('create books...')

except sqlite3.OperationalError:
    pass


# берем данные из таблицы
cur = c.execute("SELECT * FROM students")

# берем 1-ую запись (строку) из таблицы
#print(c.fetchone())

# получаем количество записей в таблице
print('rowcount:', cur.rowcount, 'description:', cur.description)


#c.execute("schema students")
#print(c.fetchone())



# закрываем соединение
conn.close()



