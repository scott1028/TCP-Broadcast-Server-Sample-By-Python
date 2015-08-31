#!/usr/bin/python
# ref: https://pymotw.com/2/socket/uds.html
# ref: https://docs.python.org/2/library/os.html#os.fork


import time
import socket
import os


parent_pid = os.getpid()
print 'Parent PID: ', parent_pid
# Share memory end


#
fd = open('./README.md', 'r')


# Fork memory for per process start
print 'Before .fork()'
pid = os.fork()
print 'After .fork()'
print pid, parent_pid


if pid == 0:
    # pid == 0
    print 'in child', os.getpid(), parent_pid
    print  'child=>\n', fd.read()
    fd.close()
else:
    # pid != 0
    print 'in parent', os.getpid(), parent_pid
    raw_input('Wait child...\r\n')
    exit(0)
    # print 'parent=>\n', fd.read()
    # fd.close()

# share read pointer, so if parent read, child will get nothing.