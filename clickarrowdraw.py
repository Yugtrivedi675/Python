import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('red')
t.pencolor('yellow')
def up():
    t.forward(50)
def left():
    t.left(90)
def right():
    t.right(90)
def move(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
def thicker():
    t.width( t.width() + 2  )
def thinner():
    t.width(  t.width() - 2)
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(thicker, ">")
turtle.onkeypress(thinner, "<")
turtle.listen()
turtle.onscreenclick(move)

