str = 'Python prograaming is easy!'
print(str.count('i'))
print(str.find("o"))
print(str.rfind("o"))  #가장 나중에 나오는 인덱스 반환
print(str.index("on"))

x= 'a bc'
print(x.split()) #['a', 'bc']

print('*'.join('hello')) #사이사이에 *를 집어넣음
print('12'.zfill(5))    #왼쪽을 0으로 채워 5자리를 만듬

print('123'.rjust(6))   #6자리를 오른쪽정렬
print('123'.center(6))