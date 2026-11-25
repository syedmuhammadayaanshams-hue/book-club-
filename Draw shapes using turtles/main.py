import turtle

t.speed(5)
t.pensize(3)

t.penup()
t.goto(-200, 50)
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(0, 50)
t.pendown()

for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(80)
    t.right(90)

t.penup()
t.goto(-200, -120)
t.pendown()

for i in range(4):
    t.forward(100)
    t.right(90)


t.penup()
t.goto(100, -120)
t.pendown()
t.circle(50)

t.hideturtle()
turtle.done()