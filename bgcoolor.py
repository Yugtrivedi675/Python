import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
color = ["red","blue","yellow","green"]
for x in range(100):
    t.pencolor( color[ x % 4] )
    t.forward(2*x)
    t.left(91)
    
