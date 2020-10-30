food = {"자장면":"단무지",
        "라면":"김치",
        
"학식":"",
        "떡볶이":"어묵",
        "삼겹살":"상추",
        "피자":"피클",
        "":"콜라"

}
'''
#for x in food :
    #print(x, end=' ') #키
    #print(food[x], end=' ') #value
'''
'''
food_list = list(food.keys())
print(sorted(food_list)) # 정렬은 리스트에서
'''
'''
import operator
sorted_food = sorted(food.items() , key = operator.itemgetter(0)) #key는 0 value는 1
print(sorted_food)
'''
for x in food : #비어있는 value의 키 출력
    if food[x] == '':
        print(x)