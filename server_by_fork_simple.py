# coding: utf-8

#!/usr/bin/python
# ref: https://pymotw.com/2/socket/uds.html
# ref: https://docs.python.org/2/library/os.html#os.fork
# fork 前的變數記體狀態將會是一個一模一樣的副本給 Child, 剛好讓 Child Parent 共用與溝通
# 模擬類似 Apache 的 Multi-Process 的 Fork 架構


import random
import time
import socket
import os


# 
def clientHandler(client, addr, server):
    while True:
        time.sleep(0.001)
        data = client.recv(1024)
        print 'Server recv: ', [data]
        client.send('Server(%s) send: ' % os.getpid() + data);
        if data == 'exit\r\n':
            client.close()
            return


# To launch Socket Server
server = socket.socket()
host = socket.gethostname()
port = int(random.random()* 10000)  # 123456
server.bind(('127.0.0.1', port))
server.listen(5)
print 'Server FD No: ', server.fileno(), ', port: ', port


parent_pid = os.getpid()
print 'Parent PID: ', parent_pid
# Share memory end


while True:
    time.sleep(0.001)
    client, addr = server.accept()
    pid = os.fork()
    if pid == 0:
        # This process is child
        print 'Fork and got connection from', addr
        clientHandler(client, addr, server)
    else:
        # This process is parent
        pass
