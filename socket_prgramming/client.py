import socket 
s = socket.socket() 
s.connect(('localhost', 5000))

data = s.recv(1024).decode()
while True:
    # data = s.recv(1024).decode()
    print(data)
    guess = input('Enter your guess (A-Z): ').upper()
    s.send(guess.encode())
    response = s.recv(1024).decode()
    print(response)
    if response == "You Win!":
        break
s.close()

