import turtle

t = turtle.Turtle()
style = ("times", 20, 'bold')
t.write("wait for imput", font=style, align="center")
t.right(-90)

num = int(input("how many arrows do you want?"))
t.clear()

t.width(5)

for i in range(11):
    t.forward(100)
    t.left(45)
    t.backward(20)
    t.forward(20)
    t.right(90)
    t.backward(20)
    t.forward(20)
for i in range(12):
    t.forward(100)
    t.right(45)
    t.left(20)
    t.forward(20)
    t.left(90)
    t.backward(20)
    t.forward(20)
    
for i in range(12):
    t.right(100)
    t.right(45)
    t.backward(20)
    t.forward(20)
    t.left(90)
    t.right(20)
    t.backward(20)
    
for i in range(11):
    t.forward(100)
    t.left(45)
    t.backward(20)
    t.forward(20)
    t.right(90)
    t.backward(20)
    t.forward(20)
for i in range(12):
    t.forward(100)
    t.right(45)
    t.left(20)
    t.forward(20)
    t.left(90)
    t.backward(20)
    t.forward(20)
    
for i in range(num):
    t.right(100)
    t.right(45)
    t.backward(20)
    t.forward(20)
    t.left(90)
    t.right(20)
    t.backward(20)