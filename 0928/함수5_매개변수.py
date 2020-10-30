'''
#딕셔너리
def dicP(**keywords):
    for i in keywords.keys():
        print(keywords.value())

dicP()
'''
#포인터가 없다면 data를 만들어 보내야되지만
#포인터가 있다면 함수의 매개변수가 괄호로 데이터를 집어 넣으면 컴퓨터가 알아서 리스트를 생성해 넣음
#버블정렬, 리스트
def bubble(alist):
    for p in range(5):
        for i in range(5):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

data = [28,15,10,25,32,17]
bubble(data)
print(data)