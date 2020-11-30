#client_time
import socket
sock = socket.socket() #인수 생략 가능
address = ('localhost', 4444)
sock.connect((address))
print("현재 시간: ", sock.recv(1024).decode())