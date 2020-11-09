import socket
ip = '127.0.0.1'
port = 4444

#클라이언트 소켓 생성
client = socket.socket()

#서버 접속
client.connect((ip,port))
print('server connect...')

#send 통해 소켓에 바이트 데이터를 전송한다
client.sendall(b'send MSG from client')
print('send msg')

#메시지 수신
msg = client.recv(1024)
print('=== msg receive')

client.close()