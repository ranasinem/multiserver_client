from time import sleep
import socket

HOST = '192.168.1.103'  # The server's hostname or IP address
PORT = 16010           # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
  data= "rana"
  data = data.encode()
  s.sendall(data)
  data = s.recv(1024)
  print('Received', repr(data))