import socket
table = {"사과의 영어 스펠링":"apple", "초대 조선왕 본명":"이성계","5000원 지폐의 인물 이름":"이이"}

s = socket.socket()
address = ("127.0.0.1", 4444)
s.bind(address)
s.listen()
print("Waiting for client")

conn, (remotehost, remoteport) = s.accept()
print("connected by", address)

i = 1;
for key in table:
    #통신1
    try:
        msg = "%d번째 문제: %s" %(i, key)
        conn.send(msg.encode())       
        data = conn.recv(1024).decode()
        #통신 2
        if table.get(key) == data:
            conn.send("정답".encode())
        else:
            conn.send("실패".encode())
            
        next = conn.recv(1024).decode()
        if next == 'q' or next =='Q':
            conn.close()
        else:
            i = i+1
    except Exception as e:
        print("연결이 종료되었습니다") #연결 강제 종료
        conn.close()
        break
    




