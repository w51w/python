from parkModule import *

category = int(input('1. 일반 입장권\n2. 자유이용권\n3. 2일 자유이용권\n4. 콤비권\n=>'))
day = input('(주간 / 야간)>')
age = int(input('나이>'))

if(category == 1):
    print("구분: 일반 입장권")
    print("주야간 : %s\n나이 : %d\n입장료는 %d입니다" %(day, age,cal_fee1(day,age)))
elif(category ==2):
    print("구분: 자유이용권")
    print("주야간 : %s\n나이 : %d\n입장료는 %d입니다" %(day, age,cal_fee2(day,age)))
elif(category ==3):
    print("구분: 2일 자유이용권")
    print("주야간 : %s\n나이 : %d\n입장료는 %d입니다" %(day, age,cal_fee3(age)))
else:
    print("구분: 콤비권")
    print("주야간 : %s\n나이 : %d\n입장료는 %d입니다" %(day, age,cal_fee4(age)))



