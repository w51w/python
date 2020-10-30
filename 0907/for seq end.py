
for i in [1,2,3]: #리스트의 길이만큼
    print('숫자' ,i)  #공백 있는 줄내림
    print('숫자' ,i, end='')  #줄내림 없음
    print('숫자' ,i, sep='')  #자동 띄어 쓰기
    print('숫자' ,i, end=' ',sep='') #

'''
for i in range(1,5) : #1~4
    print(i,end='') 
print()
for i in range (1,9,2) :
    print(i, end='')
print()
for i in range(5) : #0~4
    print(i, end='')
'''
'''
sum=0
for i in range(1,101) :
    sum += i
print('sum=', sum)
'''
'''
x=int(input('x: '))
n=int(input('n: '))
multi = x
for i in range(1,n+1):
    print(i,'번',x)
    x = x*multi
    i+=1
'''