# Autor: Alexander Herbrich
# Wann: 10.02.16
# Thema: Turtle "Honeycomb"

from turtle import *
from math import sqrt

# ========================
# = Draws a single petal =
# ========================

def drawFlower(a="orange", b="brown", penSize=2.5, size=80, rightTurn=False):
    color(b,a)
    pensize(penSize)
    begin_fill()
    pd()
    for i in range(0,6):
        rt(60) if (rightTurn) else lt(60) 
        fd(size)
    pu()
    end_fill()

def goHome(offsetX=0, offsetY=0):
    home()
    fd(offsetX)
    lt(90)
    fd(offsetY)
    rt(90)

# ========================
# = Draws a whole flower =
# ========================
def flower(drawFlower,size=80, offsetX=0, offsetY=0):
    base = size * sqrt(3)
    
    # Erstes Sechseck
    pu()
    goHome(offsetX, offsetY)
    fd(base/2)
    lt(90)
    fd(size/2)
    drawFlower("gold", size=size)

    # Zweites Sechseck
    pu()
    goHome(offsetX, offsetY)
    lt(90)
    fd(size*2)
    drawFlower(size=size)

    # Drittes Sechseck
    pu()
    goHome(offsetX, offsetY)
    lt(180)
    fd(base/2)
    rt(90)
    fd(size/2)
    drawFlower(size=size)
    
    # Viertes Sechseck
    pu()
    goHome(offsetX, offsetY)
    rt(90)
    fd(size*2)
    drawFlower(size=size,rightTurn=True)

    # Fuenftes Sechseck
    pu()
    goHome(offsetX, offsetY)
    rt(90)
    fd(size*2)
    drawFlower(size=size)

    # Sechstes Sechseck
    pu()
    goHome(offsetX, offsetY)
    fd(base/2)
    lt(90)
    fd(size/2)
    drawFlower(size=size,rightTurn=True)

    # Siebtes Sechseck
    pu()
    goHome(offsetX, offsetY)
    lt(90)
    fd(size*2)
    drawFlower(size=size,rightTurn=True)

speed(0)
size = numinput("Laenge der Kanten","Wie lang soll die Kantenlaenge sein?")
flower(drawFlower, size=size, offsetX=0, offsetY=0)
flower(drawFlower, size=size, offsetX=size*3*sqrt(3), offsetY=0)
flower(drawFlower, size=size, offsetX=size*1.5*sqrt(3), offsetY=size*4.5)
flower(drawFlower, size=size, offsetX=size*1.5*sqrt(3), offsetY=-size*4.5)
flower(drawFlower, size=size, offsetX=-size*3*sqrt(3), offsetY=0)
flower(drawFlower, size=size, offsetX=-size*1.5*sqrt(3), offsetY=size*4.5)
flower(drawFlower, size=size, offsetX=-size*1.5*sqrt(3), offsetY=-size*4.5)
flower(drawFlower, size=size, offsetX=0, offsetY=0) 