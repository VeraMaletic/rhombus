import turtle



screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("yellow")


t = turtle.Turtle()


#rectangle
t.setheading(45)
t.penup()
t.goto(-70,0)
t.pencolor("cyan")
t.pendown()
t.fillcolor("cyan")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()


#rectangle
t.setheading(45)
t.penup()
t.goto(70,0)
t.pencolor("brown")
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()


t.hideturtle()


turtle.done()