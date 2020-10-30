'''
def my_func(param):
    param = "함수 안에서 생성"
    print(param)

param ="함수 밖에서 생성"
my_func(param)
print(param)
'''
def my_func():
    global param
    param = '함수 안에서 변경'
    print(param)
    
param='함수 밖에서 생성'

print(param)
my_func()
print(param)