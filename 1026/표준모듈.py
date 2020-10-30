from os import *
from random import *
from time import *
from calendar import *

# system('calc')
#system('notepad')

#print(randint(1,5)) # 1~5
#print(randrange(1,5,2)) #step= 2

'''
start = time() #1970.01.01 자정부터 #지금까지의# 흘러온 절대시간을 초단위로 출력
for i in range(1000):
    #print(i)
    pass
end = time()

print(end-start) #출력시간을 구할 수 있다.
'''

print(asctime())
print(localtime())
myTime = localtime()
print(myTime[0],"년",myTime[1],"월",myTime[2],"일",myTime[3],"시",myTime[4],"분",myTime[5],"초")

a=['년','월','일','시','분','초']
for i in range(6):
    print(myTime[i], a[i])


cal = month(2003,12)
print(cal)
