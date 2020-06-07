import turtle
t=turtle.Pen()
number = int(turtle.numinput("number of sides or circles",
             "how many sides or circles in your shape?", 6))
shape = turtle.textinput("which shape do you want"
                         "enter 'p' for polygon or 'r' for rosette:")
for x in range(number):
    if shape == 'r':
        t.circle(100)
    else:
        t.forward (150)
    t.left(360/number)
    
