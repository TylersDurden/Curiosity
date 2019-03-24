import threading
import socket
import time


def basic_handler(client):
    try:
        print client.recv(1024)
        # Choose a response based on request?
        client.send('ACK')
        client.close()
    except socket.error:
        return False
    return True


def start_server(port, timeout):
    t0 = time.time()
    addr = '0.0.0.0'
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((addr, port))
    server_sock.listen(timeout)
    len_server = timeout*100

    while (time.time()-t0) <= len_server:
        try:
            client, address = server_sock.accept()
            print "Accepted connection from %s:%d" % (address[0], address[1])
            req = threading.Thread(target=basic_handler, args=(client,))
        except socket.error and KeyboardInterrupt:
            server_sock.close()
    server_sock.close()
    return 0


try:
    start_server(9876, 100)
except socket.error:
    time.sleep(10)
    start_server(9876, 100)

