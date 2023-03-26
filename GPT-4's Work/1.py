import turtle

def draw_circle(radius, angle, direction):
    if direction == "left":
        turtle.circle(radius, angle)
    else:
        turtle.circle(-radius, angle)

def draw_ear(size):
    turtle.begin_fill()
    turtle.forward(size)
    draw_circle(size / 2, 180, "left")
    turtle.forward(size)
    turtle.left(180)
    draw_circle(size / 2, 180, "right")
    turtle.end_fill()

def draw_head():
    turtle.begin_fill()
    draw_circle(100, 180, "left")
    turtle.left(45)
    draw_ear(100)
    turtle.left(90)
    draw_ear(100)
    turtle.left(45)
    draw_circle(100, 180, "right")
    turtle.end_fill()

def draw_body():
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(200)
    turtle.left(110)
    draw_circle(400, 100, "left")
    turtle.left(120)
    draw_circle(400, 100, "left")
    turtle.left(110)
    turtle.forward(200)
    turtle.end_fill()

def draw_tail():
    turtle.right(90)
    turtle.forward(50)
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(200)
    draw_circle(50, 180, "left")
    turtle.forward(200)
    turtle.left(180)
    draw_circle(50, 180, "right")
    turtle.end_fill()

turtle.speed(1)
turtle.bgcolor("sky blue")

turtle.color("black", "orange")
draw_head()

turtle.color("black", "yellow")
draw_body()

turtle.color("black", "brown")
draw_tail()

turtle.hideturtle()
turtle.done()
