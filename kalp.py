import turtle
import time
kalem = turtle.Turtle()

kalem.speed(10)
kalem.hideturtle()
def curve():
    for i in range(200):
        kalem.right(1)
        kalem.forward(1)
def heart():
    kalem.fillcolor('red')
    kalem.begin_fill()
    kalem.left(140)
    kalem.forward(113)
    curve()
    kalem.left(120)
    curve()
    kalem.forward(112)
    kalem.end_fill()

def txt():
    kalem.up()
    kalem.setpos(-68, 95)
    kalem.down()
    kalem.color('lightgreen')
    kalem.write("SENI SEVIYORUM", font=("Verdana", 12, "bold"))


heart()
txt()
time.sleep(10)

#Created By CyberWorldTR