t1 = (1,2,3)
print(type(t1))

l1 = list(t1) #튜플 -> 리스트
l1.append(4)  #4추가
t1 = tuple(l1)#리스트 -> 튜플
print(t1)
print(type(t1))