import socket
ip = '172.16.52.145'
port = 4444

#클라이언트 소켓 생성
client = socket.socket()

#서버 접속
client.connect((ip,port))
print('server connect...')

#send 통해 소켓에 바이트 데이터를 전송한다
client.sendall('최종찬' .encode())
print('메시지를 보냈습니다.')

#메시지 수신
msg = client.recv(1024)
print('서버로부터 받은 메시지 :', repr(msg.decode()))

client.close()