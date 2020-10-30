time = int(input('시각입력(1~12):'))
sort = int(input('am(1) or pm(2) :'))
aftertime = int(input('얼마나 지났습니까?'))

if ((time + aftertime) > 12) :
    new = (time + aftertime) - 12
    if(sort == 1):
        c = 'pm'
    else :
        c = 'am'
    print('새로운 시각은:',new,c)
else:
    if(sort == 1):
        c = 'am'
    else :
        c = 'pm'
    print('새로운 시각은:',(time + aftertime),c)