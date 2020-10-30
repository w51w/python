#일반
def cal_fee1(day,age):
    if day == "주간":
        if 12<= age < 65:
            money = 26000
        else:
            money = 19000
    else:
        if age <= 12 and age>65:
            money = 21000
        else:
            money = 16000
    return money
#자유
def cal_fee2(day,age):
    if day == "주간":
        if 12<= age < 65:
            money = 33000
        else:
            money = 24000
    else:
        if 12<= age < 65:
            money = 28000
        else:
            money = 21000 
    return money
#2일 자유
def cal_fee3(age):
    if 12<= age < 65:
        money = 55000
    else:
        money = 40000
    return money
#콤비
def cal_fee4(age):
    if 12<= age < 65:
        money = 54000
    else:
        money = 40000
    return money

if __name__ == '__main__':
    print("자유이용권 낮 소인 %d" %cal_fee2("day", 66))