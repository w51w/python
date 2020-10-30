a=[] #빈리스트
for i in range(0,50): #0~49
    a.append(i)
print(a)
#아래도 과제
# 1~50 가지 수의 제곱으로 구성되는 리스트

a=[]
for i in range(1, 51):
    a.append(i**2)
print(a)

#L=[1,2,3] M=[4,5,6] LM=[5,7,9]인 리스트 만들기
L=[1,2,3]
M=[4,5,6]
LM=[]
for i in range(0,3):
    LM.append(L[i] + M[i])
print(LM)

#과제는 날짜별로 출력해서 제출