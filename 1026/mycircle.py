def circle_area(r):
    result = r*r*3.14
    return result
def circle_circum(r):
    result = 2*3.14*r
    return result

#모듈기능을 테스트하기 위해 사용 직접 호출하여 바로 실행
if __name__ == '__main__':
    print(circle_area(4))
    print(circle_circum(5))