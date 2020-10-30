score = int(input('학점 입력:'))

if (score >= 80) :
    print('졸업반 입니다.')
elif (score >= 40 and score < 80) :
    print('2학년입니다.')
else :
    print('1학년입니다.')