
from threading import Thread
from time import sleep
import math
from random import random

from screen import Screen

flag1 = [
    [ 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 4, 7, 4, 7, 4, 7, 4, 4, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 4, 4, 7, 4, 7, 4, 7, 4, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 4, 7, 4, 7, 4, 7, 4, 4, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

flag2 = [
    [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7],
    [ 7, 7, 7, 7, 7, 7, 6, 7, 6, 7, 7, 7, 7, 7, 7, 7],
    [ 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7],
    [ 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [ 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
]

scr = Screen(80,50)
scr.draw()

threads_up = True

def render_forever():
    global scr
    while threads_up:
        scr.draw()
        sleep(0.1)

thread = Thread(target = render_forever)
thread.start()

dx = (random() * 2 + 1) - 1.5
dy = (random() * 2 + 1) - 1.5
x = 20
y = 20
ang = 0.0
dAng = math.pi / 45.0

while True:
    x += dx
    y += dy

    if (x < 5 or x > 60):
        dx = -dx
    if (y < 5 or y > 40):
        dy = -dy

    xx = math.cos(ang) * 60
    yy = math.sin(ang) * 60
    ang += dAng

    scr.clear()

    scr.img(5, 5, flag2)

    scr.setColor(5)
    scr.line(int(round(40 + xx)), int(round(25 + yy)), int(round(40 - xx)), int(round(25 - yy)))
    scr.line(int(round(40 - xx)), int(round(25 + yy)), int(round(40 + xx)), int(round(25 - yy)))

    scr.setColor(2)
    scr.circle(40, 25, 5, True)

    scr.setColor(5)
    scr.circle(40, 25, 5)
    scr.circle(40, 25, 2, True)

    scr.img(int(round(x)), int(round(y)), flag1)
    sleep(0.1)
