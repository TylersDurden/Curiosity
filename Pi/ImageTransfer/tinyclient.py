import matplotlib.pyplot as plt
import socket
import time
import os

START = time.time()
remote_host = '192.168.1.217'
remote_port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_host, remote_port))
s.send('START')
session_key = s.recv(1024)
s.close()
print "[*] Session Key Recieved "

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((remote_host, remote_port))
s1.send(session_key+'=SNAP')
token = s1.recv(1024)
s1.close()

print "[*] Server Token Acquired"
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((remote_host, remote_port))
s2.send((token))
img_file = s2.recv(1024)
s2.close()

os.system('sh tx.sh '+img_file)
image = plt.imread('test.png')

kill_switch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kill_switch.connect((remote_host, remote_port))
kill_switch.send(session_key)
print kill_switch.recv(1024)
print "====================================="
print '\033[1mFINISHED: \033[31m['+str(time.time()-START)+'s Elapsed]'

plt.imshow(image)
plt.show()
