
try:
    num = int(input('숫자를 넣으세요'))
    a=1/num
    
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다' ,e)
except ValueError as e:
    print('알 수 없는 에러', e)
else:
    print(a)