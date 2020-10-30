'''
#반환 값 없는 함수
def welcome(name):
    print("hello", name)
    return 

welcome('홍길동')

#반환 값 있는 함수
def sum(n):
    tot = 0
    for i in range(1,n+1):
        tot += i
    return tot

result = int(input("숫자입력"))
print(sum(result))
'''
def star(row, col):
    for i in range(row):
        for j in range(col):
            print("*",end="")
        print('')
    
    return
            
row = int(input("행 입력"))
col = int(input("열 입력"))
star(col, row)