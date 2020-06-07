import turtle
t=turtle.Pen()
t.speed(0)
number_of_circles = int(turtle.numinput("number of circles",
                                        "how many circles in your rosette?",6))
colors = ["red","yellow","blue","green",
          "orange","purple","white","grey"]
for x in range(number_of_circles):
    t.circle(100)
    t.left(360/number_of_circles)
                                        
