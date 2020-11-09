#한글
import socket
#서버소켓준비
server=socket.socket()
server.bind(('127.0.0.1',4444))
server.listen(1)
print('server ready...')
#클라이언트 접속 수락
while True:
    client, addr = server.accept()
    print('-----client is connected')
#메시지 수신
    print('나는 서버입니다.')
    while True:
        msg = client.recv(1024)
        print('클라이언트로 부터 메시지 수신' , repr(msg.decode()))

#메시지 송신
    print('클라이언트로 메시지 송신', addr)
    if msg:
        client.sendall('안녕 나느 서버야' .encode())
        print('메시지를 보냈습니다.')
    else :
        print('no Data', addr)
        break
client.close()
server.close()


