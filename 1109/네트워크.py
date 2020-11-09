import ipaddress
import binascii

ADDRESSES=[
        '172.16.52.149',
        'fe80::9851:5bae:aec6:dd04',
    ]
for ipaddr in ADDRESSES :
    addr = ipaddress.ip_address(ipaddr)
    print(addr)
    print('IP version  :', addr.version)
    print('Integer addr:', int(addr))
    print('Is private? :', addr.is_private) #사설망
    print('Is private? :', addr.is_global) #공중망
    print('--------------------------')
    
print("정수형 :"+str(ipaddress.ip_address(2886743189)))
print("정수형 :"+str(ipaddress.ip_address(338288524927261089664994551414041009412)))