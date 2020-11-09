import socket
'''
#호스트 정보를 튜플로 반환
hostname, aliases, addresses = socket.gethostbyaddr('127.0.0.1')
print('Hostname :',hostname)
print('Aliases :',aliases)
print('Addresses :',addresses)
'''

HOSTS = [
        'www.kopo.ac.kr',
        'www.naver.com',
        'www.google.com',
        'test'
    ]

for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        #print(host, socket.gethostbyname(host)) # 호스트 이름을 문자열 주소 변환
        print(' Hostname:', name)
        print(' Aliases:', aliases)
        print(' Addresses:', addresses)
        print(socket.getfqdn(host)) #google은 약식 서버 사용
    except socket.error as emsg:
        print('ERROR', emsg)
    print()

'''
print(socket.gethostname()) #자신의 호스트 컴퓨터 이름
#호스트 이름 => 문자열 주소 변환
host = socket.gethostname()
print(socket.gethostbyname(host))
#cmd > ipconfig 비교
'''
'''
#완전한 도메인 이름 검색
print(socket.getfqdn('kopo.ac.kr'))
print(socket.getfqdn('www.twitch.tv'))
print(socket.getfqdn('www.google.com'))
'''