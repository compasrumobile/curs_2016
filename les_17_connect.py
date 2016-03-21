# coding: utf-8
import sqlite3


class ExampleConnect:


    def __init__(self):
        # открываем или создаем базу
        self.__conn = sqlite3.connect('example.db')

        # создаем курсор - точка доступа к таблице БД
        self.__cursor = self.__conn.cursor()


    def __del__(self):
        # деструктор

        print('Закрываем соединение...')

        # закрытие соединения
        self.__conn.close()


    def select(self):
        'получаем студентов'
        for row in self.__cursor.execute("SELECT * FROM students"):
            print(row)


    def create(self):
        '''
        Создание базы данных
        :return: None
        '''

        self.__create_table('students')
        self.__create_table('books')

        # Добавление данных
        #self.__cursor.execute("INSERT INTO students VALUES (0, 'Ivan', '1980-01-05')")
        #self.__cursor.execute("INSERT INTO students VALUES (1, 'Mariya', '1985-03-15')")

        # добавлять массивы данных
        self.__cursor.executemany("insert into students values (?, ?, ?)", [
            (0, 'Ivan', '1980-01-05'),
            (1, 'Mariya', '1985-03-15')
        ])

        self.__conn.commit()


    def __create_table(self, table_name):

        try:
            # создаем таблицу
            self.__cursor.execute('CREATE TABLE {} (id INTEGER, name text, date text)'.format(
                table_name))

            # сохраняет изменения в БД
            self.__conn.commit()

            print('create {}...'.format(table_name))

        except ImportError: #sqlite3.OperationalError:
            pass



if __name__=='__main__':

    connect = ExampleConnect()

    print(connect.select.__doc__)
    print(connect.create.__doc__)