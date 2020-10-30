class Animal:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind
    def sound(self):
        pass
    def display(self):
        print("이름:", self.name)
        print("나이:", self.age)
        print("종류:", self.kind.aname)
        self.kind.sound()
class Dog:
    aname="강아지"
    def sound(self):
        print("멍멍")
class Cat:
    aname="고양이"
    def sound(self):
        print("야옹")
        
mydog = Animal("쫑", 5, Dog())
mydog.display()

mycat = Animal("냥이", 3, Cat())
mycat.display()
        