import turtle

t = turtle.Turtle()

style = ("times", 20, 'bold')
t.write("wait for imput", font=style, align="center")
t.right(-90)

num = int(input("how manyarrows do you want?"))
t.clear()

t.width(5)

for i in range(num):
    t.forward(100)
    t.left(45)
    t.backward(20)
    t.forward(20)
    t.right(90)
    t.backward(20)
    t.forward(20)
from turtle import *
win = Turtle()
done()