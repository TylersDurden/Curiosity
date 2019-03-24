import threading
import socket
import time

remote_host = '192.168.1.217'
remote_port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_host, remote_port))
s.send('START')
session_key = s.recv(1024)
s.close()

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((remote_host, remote_port))
s1.send(session_key+'=SNAP')
print s1.recv(1024)
s1.close()
