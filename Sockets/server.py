from socket import socket

s = socket()

print('socket created')


s.bind(('localhost', 9999))

s.listen(3)
print('waiting for the connection...')

while True:

    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with", addr)


    c.send(bytes('Welcome to server', 'utf-8'))
    c.close()