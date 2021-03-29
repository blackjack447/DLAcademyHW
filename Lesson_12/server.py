import socket
import time
import json


host = 'localhost'
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print('Сервер - запустился !')
quit = False

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsstime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())
        print('[' + addr[0] + ']=[' + str(addr[1]) + ']=[' + itsstime + ']/', end='')
        print(data.decode('utf-8'))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except Exception as e:
        print(e)
        quit = True

    s.close()

    print('Сервер - остановлен!')