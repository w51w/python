leng = float(input('cm 입력:'))

if (leng <= 0) :
    print('잘못 입력하였습니다')
else :
    inch = leng / 2.54
    print('%.1f' %inch)
