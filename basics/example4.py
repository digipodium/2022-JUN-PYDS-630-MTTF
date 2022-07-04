from turtle import *

t = Turtle()
t.speed('fast')

bgcolor('black')
t.color('yellow')
t.pensize(12)

for i in range(1,501,3):
    t.fd(i)
    t.lt(60)

mainloop()
