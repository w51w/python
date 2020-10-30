from random import randint
rNum = randint(1,10) #1~50

count = 0
#5개 입력할때까지 랜덤한 값 맞추기
print("1~10 랜덤 값 맞추기")
while True:
    answer = int(input("정수입력"))
    if((answer != rNum)):
        print("%d는 오답입니다."%(answer))
        count=count+1
        if(count ==5):
            print("실패 , 5번 모두 입력했습니다")
            break;
    else :
        print("정답입니다")
        break;
