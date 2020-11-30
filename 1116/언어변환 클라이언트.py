import socket
address = ("localhost", 4444)
s = socket.socket()
s.connect(address)
while True:
    msg = input("Message to send : ")
    try:
        n = s.send(msg.encode()) #메시지 전송
    except:
        print("송신 연결이 종료되었습니다")
        retry = input("계속?(y/n) ")
        if retry == 'n': #연결 종료
            s.close()
            break
        else: #메시지 전송 계속
            continue
    else:
        print("{} bytes sent".format(n)) #전송된 바이트 수
    s.settimeout(3.0) # 타임아웃 3초
    try:
        data = s.recv(1024) #receive message from server
        if not data: break
        if msg == 'q' or msg == 'Q':
            break

    except:
        print("수신 연결이 종료되었습니다")
        s.close()
        break
    else:
        print("Received message: %s" %data.decode())
