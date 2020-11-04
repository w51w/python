def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False

assert isEven(81) # 조건이 False이면 예외 발생
print('Even')