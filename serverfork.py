#!/usr/bin/python
# ref: https://pymotw.com/2/socket/uds.html


import socket
import os


# Share memory start
parent, child = socket.socketpair()

parent_pid = os.getpid()
print 'Parent PID: ', parent_pid
# Share memory end


# Fork memory for per process start
print 'Before .fork()'
pid = os.fork()
print 'After .fork()'
print pid, parent_pid


if pid:
    # pid == 0
    print 'in parent, sending message'
    child.close()
    parent.sendall('ping')
    response = parent.recv(1024)
    print 'response from child:', response
    parent.close()

else:
    # pid != 0
    print 'in child, waiting for message'
    parent.close()
    message = child.recv(1024)
    print 'message from parent:', message
    child.sendall('pong')
    child.close()
# Fork memory for per process end