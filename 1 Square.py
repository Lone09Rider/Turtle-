import turtle

design = turtle.Turtle()

design.color("cyan")
design.speed(2)
design.begin_fill()

design.forward(100)
design.left(90)
design.forward(100)
design.left(90)
design.forward(100)
design.left(90)
design.forward(100)
design.penup()
design.forward(150)
design.pendown()

design.end_fill()
turtle.done()
