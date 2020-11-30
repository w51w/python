import socket

s = socket.socket()
address = ("127.0.0.1", 4444)
s.bind(address)
s.listen()
print("Waiting for client")

conn, address = s.accept()
print("connected by", address)
while True:
    try :
        data = conn.recv(1024) #수신할 때 예외 #(버퍼 사이즈)
    except Exception as e:
        print("연결이 종료되었습니다") #연결 강제 종료
        conn.close()
        break
    else :
       print(data.decode())   
    try :
        conn.send(data) #송신할 때 예외
    except:
        print("연결이 종료되었습니다")
        conn.close()
        break

