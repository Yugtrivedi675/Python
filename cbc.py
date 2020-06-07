import turtle
t=turtle.Pen()
turtle.bgcolor("pink")
t.speed(0)
colors = ["red","blue","yellow","green","orange"]
for x in range(1000):
    t.pencolor(colors[x % 4] )
    t.circle(x)
    t.left(91)
