'''
friend=['하나','둘','셋']
print(friend)
friend.insert(0, '넷')
print(friend)
friend.insert(2, '다섯')
friend.append('여섯')
print(friend)
'''
list = [1,2,3]
list[1] = 17
print(list + [4,5,6]) #저장안됨
print(list)
list[3:6]=[4,5,6]
print(list)
list[0:1]=[] #첫번째 요소 제거
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.insert(3,25)
print(list)