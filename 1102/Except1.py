import sys
try:
    fp = open('t.txt')
    sl = fp.readline() #파일이 없으면 os 오류
    sl = int(fp.readline()) #한줄 읽기
    value = sl.strip() #공백 ,개행문자 지움
    
except OSError as err:
    print('OS 오류 :', err)
except ValueError as v:
    print('정수로 변화 불능', v)
except:
    print('알 수 없는 예외')
else:
    print(value)
finally:
    print("예외 처리 끝")
