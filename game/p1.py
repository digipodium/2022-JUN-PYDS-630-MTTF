import pgzrun

WIDTH = 500
HEIGHT = 500

box = Rect((40,50),(100,100))

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'red')

def update():
    box.x += 5
    if box.x > WIDTH:
        box.x = 0
    if box.x < 0:
        box.x = WIDTH

pgzrun.go()