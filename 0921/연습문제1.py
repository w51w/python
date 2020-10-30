days = {'January':31,
        'February':28,
        'March':31,
        'April':30,
        'May':31,
        'June':30,
        'July':31,
        'August':31,
        'September':30,
        'October':31,
        'November':30,
        'December':31}

#1. 월 입력 일수 출력
'''
mon = input("월 입력")
print(days.get(mon))
'''
#2. 알파벳 순서로 모든 월 출력
'''
mon_list = list(days.keys())
print(sorted(mon_list)) # 정렬은 리스트에서
'''
#3. 일수가 31인 월 모두 출력
'''
for x in days : #비어있는 value의 키 출력
    if days[x] == 31:
        print(x, end=' ')
'''
#4. 월의 일수를 기준으로 오름차순으로 key-value 쌍을 출력
'''
import operator
sorted_days = sorted(days.items() , key = operator.itemgetter(1)) #key는 0 value는 1
print(sorted_days)
'''
#5. 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.
mon = input("월 입력(3문자):")
for x in days:
    if(mon == x[:3]):
        #print(x[:3])
        print(days.get(x))
       

