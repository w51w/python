import socket
address = ("localhost", 4444)
s = socket.socket()
s.connect(address)
while True:
    #통신1
    data = s.recv(1024).decode()
    print(data)
    msg = input("Message to send : ")
    s.send(msg.encode())
    #통신2
    next = s.recv(1024).decode()
    if next == "정답" :
        msg = input("정답입니다 그만 두려면 'q'를 계속하려면 아무키나 보내세요 : ")
        if msg == 'q' or msg == 'Q':
            break;
        s.send(msg.encode())
    else:
        print("틀렸습니다.")
        s.close()
        break;