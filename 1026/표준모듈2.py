import math

#print(dir(math))
def inputAngle(r):
    degree = r
    radian = degree * math.pi / 180
    print ("sin:" ,"%.2f" %math.sin(radian) , "cos:", "%.2f" %math.cos(radian), "degree:", r)
