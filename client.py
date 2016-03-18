# Echo client program
import socket

HOST = 'localhost'        # The remote host      127.0.0.1
PORT = 50007              # The same port as used by the server


# Создаем объект Сокета (объект соединения)
# - тип связи, тип соединения = TCP + IP, потоковое
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# соединякмся с сервером по адресу и порту
s.connect( (HOST, PORT) )

# отправляем данные - массив байтов
s.sendall(b'Hello, world')

# получаем ответ от сераера
# - 1024 - ограничение по количеству
data = s.recv(1024)

# закрываем сокет
s.close()

# вывод на экран полученных данных
print('Received', repr(data))
