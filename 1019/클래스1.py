class Car:
    color =""
    speed=()
    count=0 # 클래스변수
    def __init__(self):##초기화 == Constructor
        self.speed=0   #인스턴스 변수
        Car.count += 1 #클래스 변수


#인스턴스변수 선언
myCar1, myCar2 = None, None

#인스턴스화
myCar1 = Car();
myCar1.color = "white"
myCar1.speed =30
print("%s 자동차1의 현재속도는 %d, 생산된 자동차수는 총 %d" %(myCar1.color, myCar1.speed, Car.count))

myCar2 = Car();
myCar2.color = "black"
myCar2.speed =60
print("%s 자동차1의 현재속도는 %d, 생산된 자동차수는 총 %d" %(myCar2.color, myCar2.speed, myCar2.count))