import socket

s = socket.socket()
s.bind(('localhost', 5000))
s.listen() 
conn, addr = s.accept()
print(f"Server-side connection established from {conn}, {addr} ")
conn.send("Client connected".encode())

while True:
    pass

conn.close()
s.close()
