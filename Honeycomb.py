# Autor: Alexander Herbrich
# Wann: 10.02.16
# Thema: Turtle "Honeycomb"

from turtle import *

def flowerdraw(a = ("orange"), b = ("brown"), c = (2.5), d = (80), e = (60)):
    pencolor(b)
    pensize(c)
    fillcolor(a)
    begin_fill()
    lt(e); fd(d)
    lt(e); fd(d)
    lt(e); fd(d)
    lt(e); fd(d)
    lt(e); fd(d)
    lt(e); fd(d)
    end_fill()

def flowerdraw2(a = ("orange"), b = ("brown"), c = (2.5), d = (80), e = (60)):
    pencolor(b)
    pensize(c)
    fillcolor(a)
    begin_fill()
    rt(e); fd(d)
    rt(e); fd(d)
    rt(e); fd(d)
    rt(e); fd(d)
    rt(e); fd(d)
    rt(e); fd(d)
    end_fill()

def flower(flowerdraw, flowerdraw2):
    pu()
    fd(69)
    lt(90)
    fd(40)
    pd()
    flowerdraw(("gold"))
    end_fill()
    pu()
    home()
    # Erstes Sechseck
    pu()
    lt(90)
    fd(160)
    pd()
    flowerdraw()
    pu()
    home()
    # Zweites Sechseck
    pu()
    lt(180)
    fd(69)
    rt(90)
    fd(40)
    pd()
    flowerdraw()
    pu()
    home()
    # Drittes Sechseck
    pu()
    rt(90)
    fd(160)
    pd()
    flowerdraw2()
    pu()
    home()
    # Viertes Sechseck
    pu()
    rt(90)
    fd(160)
    pd()
    flowerdraw()
    pu()
    home()
    # Fuenftes Sechseck
    pu()
    fd(69)
    lt(90)
    fd(40)
    pd()
    flowerdraw2()
    pu()
    home()
    # Sechstes Sechseck
    pu()
    lt(90)
    fd(160)
    pd()
    flowerdraw2()
    pu()
    home()
    # Siebtes Sechseck
    pu()
    fd(34.5)
    lt(90)
    fd(20)
    pd()
    a = 1
    while (a == 1):
        pd()
        flowerdraw(("orange"), ("brown"), (2.5), (40), (60))
        pu()
    # Kleines Sechseck
flower(flowerdraw, flowerdraw2)