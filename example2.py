from turtle import *

t = Turtle()
t.speed('fastest')
s = getscreen()
for i in range(8):
    t.fd(100)
    t.lt(360//8)
    
mainloop()