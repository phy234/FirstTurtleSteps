# Autor: Alexander Herbrich
# Wann: 10.02.16
# Thema: Turtle "Hexagon"

from turtle import *

def hexagon():
    pu()
    fd(80)
    lt(90)
    fd(40)
    pd()
    pencolor("red")
    pensize(2.5)
    fillcolor("cyan")
    begin_fill()
    lt(60)
    fd(80)
    lt(60)
    fd(80)
    lt(60)
    fd(80)
    lt(60)
    fd(80)
    lt(60)
    fd(80)
    lt(60)
    fd(80)
    end_fill()
    pu()
    home()
hexagon()