import socket
import threading
import time
import json


shutdown = False
join = False

def receiving(name, sock):
    while not shutdown:
        while True:
            try:
                data, attr = sock.recvfrom(1024)
                print(data.decode('utf-8'))
            except:
                pass

server = ('localhost',9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(server)

name = input('Name: ')

rT = threading.Thread(target=receiving, args=(name, s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(('[' + name + '] => join chat').encode('utf-8'), server)
        join = True
    else:
        try:
            message = input('[You] :: ')
            if message != '':
                s.sendto(('[' + name + '] :: ' + message).encode('utf-8'))
        except Exception as e:
            s.sendto(('[' + name + '] => вышел из чата').encode('utf-8'), server)
            shutdown = True

rT.join()
s.close()
