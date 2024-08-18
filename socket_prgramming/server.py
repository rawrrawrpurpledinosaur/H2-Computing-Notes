import socket 
import random

answer = chr(random.randint(65, 90))

s = socket.socket()
s.bind(('localhost', 5000))
s.listen()
conn, addr = s.accept()
print(f"Connection from {addr} has been established")

conn.send("".encode())

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    if data == answer:
        conn.send("You win!".encode())
        break
    else:
        if data < answer:
            conn.send("The answer is after your guess".encode())
        elif data > answer:
            conn.send("The answer is before your guess".encode())
        else: 
            conn.send("Invalid input".encode())
conn.close()
s.close()

