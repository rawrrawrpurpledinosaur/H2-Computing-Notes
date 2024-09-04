import socket

s = socket.socket()
s.connect(('localhost', 5000))

data = s.recv(1024).decode()

print(data)

while True:
    pass

s.close()
