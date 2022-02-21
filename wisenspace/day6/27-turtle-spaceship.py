import turtle

print(dir(turtle))
print(turtle._ver)

screen = turtle.Screen()

screen.setup(400, 400)

screen.bgpic("../dat/space.gif")

if False:
    screen.addshape("../dat/rocketship.gif")
    turtle.shape('../dat/rocketship.gif')
else:
    turtle.shape('turtle')  # arrow, blank, circle, classic, square, triangle, turtle
    # turtle.resizemode('auto')
    # turtle.shapesize(5, 5, 12)
    turtle.color('red')

move_speed = 10
turn_speed = 10

def forward():
    turtle.forward(move_speed)

def backward():
    turtle.backward(move_speed)

def left():
    turtle.left(turn_speed)

def right():
    turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.home()

screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

turtle.mainloop()
