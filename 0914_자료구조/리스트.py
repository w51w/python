#크기상관없이 자료형 달라도 됨
a =[1,'hello',2,'world',1,23]
print(type(a))
print(a)
#삽입
a.append('append') #뒤에 추가
print(a)
a.insert(2,'insert') #2번 뒤에 삽입
print(a)
#리스트는 수정이 가능하다
a[2] = '수정'
print(a)
#인덱스 구조
##0123
##-4-3-2-1
print(a + ['저장','안','됨'])
#저장되는 것은 아님
print(a)
#삭제
a[2:6] = [] #범위 만큼만
print(a)
a[:]=[]
print(a)
