import turtle

two_squares = turtle.Turtle()

two_squares.color("blue")
two_squares.begin_fill()

two_squares.left(90)
two_squares.forward(80)
two_squares.right(90)
two_squares.forward(80)
two_squares.right(90)
two_squares.forward(80)
two_squares.right(90)
two_squares.forward(80)

two_squares.end_fill()

two_squares.penup()
two_squares.forward(80)
two_squares.pendown()

two_squares.color("red")
two_squares.begin_fill()

two_squares.left(90)
two_squares.forward(80)
two_squares.right(90)
two_squares.forward(80)
two_squares.right(90)
two_squares.forward(80)
two_squares.right(90)
two_squares.forward(80)

two_squares.end_fill()
two_squares.left(90)
two_squares.penup()
two_squares.forward(80)
two_squares.pendown()

two_squares.color("cyan")
two_squares.begin_fill()

two_squares.forward(80)
two_squares.left(90)
two_squares.forward(80)
two_squares.left(90)
two_squares.forward(80)
two_squares.left(90)
two_squares.forward(80)

two_squares.end_fill()


turtle.done()
