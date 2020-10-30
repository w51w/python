
#리스트  []
#딕셔너리{key:value}
#튜플    ()  수정x
#집합    {}  #중복되지 않고 순서없이 모아놓은 자료구조

#1부터 45 까이즹 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램
import random
pick = set()
while len(pick) < 6:
    n = random.randint(1,45)
    if n not in pick: # 중복 배제
        pick.add(n)   #집합에 요소 추가
print(pick)
print(sorted(pick))

