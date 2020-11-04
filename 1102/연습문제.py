data={"Sun":0, "Mon":1, "Tue":2, "Wed":3, "Thu":4, "Fri":5, "Sat":6}

Flag = True
while Flag :  
    day = input('입력')
    if day not in data:
        print("데이터 없음")
        Flag = False
    else:
        print(data[day])
        
'''
while True:
    try:
        num = input("입력 ")
        print(data[num])
    except:
        print("data 없음")
        break
 '''       
