def area(radius):
    if radius<0:
#        print('음수는 안됨')
        raise RuntimeError('음수는 안됨')
    
    else:
        print(3.14*radius*radius)
area(-3)