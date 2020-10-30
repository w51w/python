import turtle
def drawBarChar(t, value):
    t.begin_fill()
    t.left(90)
    t.forward(value)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(value)
    t.left(90)
    t.end_fill()

def bubble(alist):
    for p in range(6):
        for i in range(6):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

t = turtle.Pen()
data=[100,120,300,80,90,130,250]
bubble(data)

t.color('red')
t.fillcolor('blue')
t.pensize(3)

for d in data:
    drawBarChar(t, d)