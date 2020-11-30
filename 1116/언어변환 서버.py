import socket

table = {1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}

s = socket.socket()
address = ("127.0.0.1", 4444)
s.bind(address)
s.listen()
print("Waiting for client")

conn, (remotehost, remoteport) = s.accept()
print("connected by", address)
while True:
    try :
        data = conn.recv(1024) #수신할 때 예외
    except Exception as e:
        print("연결이 종료되었습니다") #연결 강제 종료
        conn.close()
        break
    else :
        print("Received message:",data.decode())
    try :
        #데이터 타입에 주의
        a = table.get(int(data.decode()))
        conn.send(a.encode()) #송신할 때 예외
        
    except:
        print("연결이 종료되었습니다")
        conn.close()
        break


