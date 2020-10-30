class Car():
    speed = 0
    def speedUp(self, value):
        self.speed += value
        print("슈퍼클래스 속도 %d" %self.speed)
class Sedan(Car):
    def speedUp(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
            print("현재속도는 %d" %self.speed)
class Truck(Car):
    pass

sedan1, truck1 = None, None

truck1 = Truck()
sedan1 = Sedan()
print("트럭->", end="")
truck1.speedUp(200)

print("세단->", end="")
sedan1.speedUp(200)
sedan1.speedUp(120)