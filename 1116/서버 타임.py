#time_server
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #인수 생략 가능
address = ('127.0.0.1', 4444)
s.bind(address)
s.listen()
while True:
    client, addr = s.accept()
    print("Connection requested from ", addr)
    client.send(time.ctime(time.time()).encode())
    client.close()
