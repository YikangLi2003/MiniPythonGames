import turtle

def draw_circle(radius, angle):
    turtle.circle(radius, angle)

def draw_ears():
    for _ in range(2):
        turtle.begin_fill()
        turtle.forward(100)
        turtle.left(50)
        turtle.forward(50)
        turtle.left(80)
        turtle.forward(50)
        turtle.left(50)
        turtle.forward(100)
        turtle.left(180)
        turtle.end_fill()

def draw_face():
    turtle.begin_fill()
    draw_circle(100, 180)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    draw_circle(100, 180)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.end_fill()

def draw_eyes():
    for _ in range(2):
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()

def draw_nose():
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

# Initial setup
turtle.speed(1)
turtle.bgcolor("sky blue")

# Draw ears
turtle.color("black", "orange")
draw_ears()

# Draw face
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("black", "yellow")
draw_face()

# Draw eyes
turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()
turtle.color("black", "white")
draw_eyes()

# Draw nose
turtle.penup()
turtle.goto(-10, 0)
turtle.pendown()
turtle.color("black", "pink")
draw_nose()

turtle.hideturtle()
turtle.done()
