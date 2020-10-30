class SuperClass:
    def __init__(self):
        self.sound()
    def sound(self):
        print("super haha")

class SubClass(SuperClass):
    def __init__(self):
        self.sound()
    def sound(self):
        #super().sound()
        print("sub haha")
sub = SubClass()