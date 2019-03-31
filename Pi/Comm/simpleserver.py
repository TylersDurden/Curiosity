from Crypto.Random import get_random_bytes
from threading import Thread
import socket
import os


def login(client, log):
    print "Client is Logging In"
    uname = ''
    passwd = ''


def client_hello(client, log, events):
    token = get_random_bytes(32)
    client.send('hello '+token)
    open(log, 'w').write(token)
    client.close()
    return token


event_handles = {'hello': client_hello}
running = True
port = 9999

# Bind a local socket as a server
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
except socket.error:
    print "Cant Start Server..."
    exit(0)
server.listen(10)
while running:
    try:
        client, addr = server.accept()
        print 'Connection Accepted from %s:%d' % (addr[0], addr[1])
        request = client.recv(512)
        log_name = addr[0].replace('.', '') + '.log'
        if request in event_handles.keys():
            token = event_handles[request](client, log_name, event_handles)
            event_handles['hello' + token] = login
        client.close()
    except socket.error or KeyboardInterrupt:
        print 'Connection Error!'
        server.close()
        running = False
