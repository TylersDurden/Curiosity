from Crypto.Random import get_random_bytes
import hashlib
import threading
import socket
import time
import os


class Server:
    # Define a shared session secret
    session_key = get_random_bytes(128)
    # Server Settings
    bind_addr = '0.0.0.0'
    port = 9999
    run_time = 0.
    looping = False
    START = 0
    token = ''

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
        print '\t* Session Key Generated'
        return self.session_key

    @staticmethod
    def check_for_image():
        if os.path.isfile('test.png'):
            return os.getcwd()+'/test.png'
        else:
            return

    @staticmethod
    def remove():
        print "Transferring test.png "
        os.remove('test.png')
        return "Good Stuff. All set on this end."

    def snap(self):
        print "\t* Snapping Image"
        os.system('raspistill -t 1 -vf -hf -f -rot 90 -o test.png -e png')
        self.token = hashlib.sha256(str(time.time())).digest()
        return self.token

    def request_handler(self, client):
        EVENT_TABLE = {'START': self.session_start,
                       self.session_key + '=SNAP': self.snap,
                       self.token: self.check_for_image,
                       self.session_key: self.remove}

        request = str(client.recv(1024))
        if str(request) in EVENT_TABLE.keys():
            client.send(EVENT_TABLE[str(request)]())
        client.close()
        return True


def main():
    Server(360, 5)


if __name__ == '__main__':
    main()
