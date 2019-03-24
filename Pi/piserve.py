from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import threading
import pisight
import socket
import time
import os


class Server:
    # Define a private session key
    session_key = get_random_bytes(128)
    # Server Settings
    bind_addr = '0.0.0.0'
    port = 9999
    run_time = 0.
    looping = False
    START = 0



    def __init__(self, run_time, timeout):
        self.initialize(run_time)
        self.run(timeout)

    def initialize(self,run_time):
        if run_time == -1:
            self.looping = True
            self.run_time = 1e6
        else:
            self.run_time = run_time

    def run(self, timeout):
        self.START = time.time()
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind((self.bind_addr, self.port))
        server_sock.listen(timeout)
        while (time.time() - self.START) <= self.run_time:
            try:
                client, address = server_sock.accept()
                print "Accepted connection from %s:%d" % (address[0], address[1])
                threading.Thread(target=self.request_handler, args=(client,)).start()
            except socket.error and KeyboardInterrupt:
                server_sock.close()
        server_sock.close()
        return 0

    def session_start(self):
        return self.session_key

    def snap():
        print "Snapping Image..."
        pisight.snap()
        return hashlib.sha256(str(time.time())).digest()

    def request_handler(self, client):
        EVENT_TABLE = {'START': self.session_start,
                       self.session_key + '=SNAP': self.snap}

        request = str(client.recv(1024))
        if str(request) in EVENT_TABLE.keys():
            client.send(EVENT_TABLE[str(request)]())
        client.close()
        return True



Server(360, 5)
