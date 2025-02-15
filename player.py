# Черепашьи гонки.

from turtle import *
from random import randint
from time import sleep

finish = 400

def startRace(t, x, y, c):
    t.speed(5)
    t.color(c)
    t.shape('turtle')
    t.penup()
    t.goto(x,y)

def drawtrack(t):
    t.color('white')
    t.speed(0)
    t.penup()
    x = -400
    y = 300
    t.goto(x,y)
    t.pendown()
    t.right(90)
    for i in range(32):
        t.forward(600)
        t.penup()
        x += 25
        t.goto(x, y)
        t.pendown()
    t.left(90)

def dance(t):
    t.penup()
    t.goto(0, 0)
    t.left(90)
    t.speed(1)
    for i in range(10):
        t.forward(30)
        sleep(0.3)
        t.back(30)
    t.pendown()
    t.speed(0)
    for i in range(70):
        t.circle(2500)
        t.left(80)

def lost(t):
    for i in range(15):
        t.speed(10)
        t.left(3600)


bgcolor('black')

t1 = Turtle()
t2 = Turtle()
drawtrack(t1)
startRace(t1, -400, 30, 'chartreuse')
startRace(t2, -400, -30, 'goldenrod')

sleep(2)
while t1.xcor() < finish and t2.xcor() < finish:
    t1.forward(randint(2,8))
    t2.forward(randint(2,8))
sleep(1)

if t1.xcor() > t2.xcor():
    print("Победила лаймовая!")
    dance(t1)
    lost(t1)
elif t2.xcor() > t1.xcor():
    print("Победила жёлто-золотая!")
    dance(t2)
    lost(t2)
else:
    print("Ничья!")
    dance(t1)
    dance(t2)

exitonclick()