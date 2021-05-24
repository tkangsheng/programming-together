import socket

PORT_NUMBER = 80
BUFFER_SIZE = 512
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', PORT_NUMBER))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) # GET is an http request

next_line_windows = '\r\n'
next_line_linux_mac = '\n'
# 4 HTTP requests: GET, POST, UPDATE, DELETE

while True:
    data = mysock.recv(BUFFER_SIZE)
    # print(f'\nI JUST RECEIVED {len(data)} BYTES\n')
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()