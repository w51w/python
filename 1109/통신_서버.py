import socket
#서버소켓준비
server=socket.socket()
server.bind(('127.0.0.1',4444))
server.listen(1)
print('server ready...')
#클라이언트 접속 수락
client, addr = server.accept()
print('-----client is connected')

#메시지 수신
msg = client.recv(1024)
print('msg received')
print(msg)

#메시지 송신
#client.sendall(b'server message\n')
client.sendall(b'hello')
#바이트단위 데이터 전
print('msg send')
client.close()
server.close()


