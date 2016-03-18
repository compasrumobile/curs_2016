# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


# создаем Сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# привязываем сокет к адресу и порту
s.bind( (HOST, PORT) )

# начинаем слушать порт и адрес
# - кол-во ожидающих соединений
s.listen(1)


while True:
    # получаем соединение
    conn, addr = s.accept()

    # отображаем
    print('Connected by', addr)

    while True:
        # получаем данные от клиента
        data = conn.recv(1024)

        if not data:
            # выходим из цикла, когда данные закончатся
            break

        # отправляем клиенту то же самое
        conn.sendall(bytearray(reversed(data)))

    # закрываем сокет
    conn.close()