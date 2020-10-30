'''
t1 = input('문자입력')
print(type(t1)) #
t1 = list(t1)
print(type(t1)) #
t1.sort()
t1 = tuple(t1)
print(type(t1)) #
print(t1)       #
'''
t1 = ('apple','grape','banana')
fruit = input('당신이 좋아하는 과일은?')
if(fruit in t1):
    print(fruit + '내가 좋아하는 과일 입니다.')
else:
    print('과일 입니다.' + fruit)