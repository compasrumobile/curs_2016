# coding: utf-8
import sqlite3

# открываем или создаем базу
conn = sqlite3.connect('example.db')

# создаем курсор - точка доступа к таблице БД
c = conn.cursor()

# получаем студентов
for row in c.execute("SELECT * FROM students"):
    print(row)


# закрываем соединение
conn.close()



