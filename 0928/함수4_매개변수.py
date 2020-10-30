'''
def prtMsg(msg, count=1):
    print(msg *count)
    
prtMsg("Hello") #msg=Hello, count =1 사용 (생략 시 기본값으로 전달)
                #msg는 값이 없으면 에러가 난다
prtMsg("Hi ", 5)

def print_language(*languages): #*arg 로 표시되면 튜플로 처리
    for lang in languages:
        print(lang)

print_language('python', 'java','android')
'''
def total(*num):
    sum=0
    for i in num:
        sum +=i
    return sum
print(total(1,2,3))
print(total(1,2,3,10,20))