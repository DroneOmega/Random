import turtle
import math

RED="#FF0000"
PINK="#ff00ff"
GREEN="#00ff00"

def drawSquare(size, colour):
    turtle.color(colour)
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def drawHouse(size, colour):
    turtle.pendown()
    turtle.color(colour)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(math.sqrt(size * size * 2))
    turtle.right(135)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(math.sqrt(size * size * 2))
    turtle.left(90)
    turtle.forward(math.sqrt(size * size * 2) / 2)
    turtle.left(90)
    turtle.forward(math.sqrt(size * size * 2) / 2)
    turtle.penup()

def drawStar():
    n = 45
    angle = 180 - 180 / n
    for i in range(n):
        turtle.forward(200)
        turtle.right(angle)

turtle.speed(100)
turtle.fillcolor(RED)
turtle.begin_fill()
drawStar()
turtle.end_fill()

#drawHouse(100, RED)

#turtle.speed(1)
#turtle.setheading(0)
#turtle.pendown()
#drawSquare(100, RED)
#turtle.penup()
#turtle.forward(90)
#turtle.right(90)
#turtle.heading()
#turtle.forward(10)
#turtle.pendown()
#drawSquare(80, GREEN)
#turtle.penup()

turtle.exitonclick()
