class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self):
        pass

class Dog(Animal):
    aname="강아지"
    def __init__(self, name, age):
        super().__init__(name,age)
    def display(self):
        print("동물명:", self.aname)
        print("이름:", self.name)
        print("나이:", self.age)
    def sound(self):
        print("멍멍")
        
mydog = Dog("쫑", 5)
mydog.display()
mydog.sound()