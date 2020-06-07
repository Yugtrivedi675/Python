import turtle
t = turtle.Turtle()
t.speed(0)
t.width(4)
colors = ["red","orange","yellow","green","blue","indigo","violet",]
for x in range(200):
    t.pencolor(colors[x%7])
    t.forward(x)
    t.left(360/7 + 1)
    
