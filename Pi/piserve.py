from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import threading
import socket
import time
import sys


class Server:
    # Define a private session key
    session_key = get_random_bytes(128)
    # Server Settings
    bind_addr = '0.0.0.0'
    port = 9999
    run_time = 0.
    looping = False
    START = 0

    EVENT_TABLE = {'START': session_key}

    def __init__(self, run_time, timeout):
        sock = self.initialize(run_time, timeout)
        self.run(sock)

    def initialize(self,run_time, timeout):
        if run_time == -1:
            self.looping = True
            self.run_time = 1e6
        else:
            self.run_time = run_time
        sock = self.start_server(timeout)
        return sock

    def run(self, server_sock):
        while (time.time() - self.START) <= self.run_time:
            try:
                client, address = server_sock.accept()
                print "Accepted connection from %s:%d" % (address[0], address[1])
                threading.Thread(target=self.request_handler, args=(client,))
            except socket.error and KeyboardInterrupt:
                server_sock.close()
        server_sock.close()
        return 0

    def start_server(self, timeout):
        self.START = time.time()
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind((self.bind_addr, self.port))
        server_sock.listen(timeout)
        return server_sock

    def request_handler(self, client):
        request = client.recv(1024)
        if str(request) in self.EVENT_TABLE.keys():
            client.send(self.EVENT_TABLE[str(request)])
        client.close()


Server(360, 5)
