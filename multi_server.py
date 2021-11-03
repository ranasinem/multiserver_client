import socket
import time
from _thread import *
import threading
from socket import gethostbyname
from datetime import datetime
print_lock = threading.Lock()
def threaded(c,addr):
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            print_lock.release()
            break
        data=data.decode()
        print("Received from", addr[0], ':', addr[1])
        print ("  ",data)
        time.sleep(1)
        print("bitti")
        c.send(data)
    c.close()

def Main(): 
    HOST = gethostbyname('0.0.0.0')  # Standard loopback interface address (localhost)
    PORT = 16010                    # Port to listen on (non-privileged ports are > 1023)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("socket binded to port", PORT)

    while True:
        s.listen(5); print("socket is listening")
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()

if __name__ == '__main__':
    Main()
