# 1. draw rectangle
"""
import turtle as t

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.mainloop()


# 2. sprial

from turtle import *

speed('fast')
for i in range(100):
    forward(i*10)
    left(91)

mainloop()

# 3. colorful hexagon spiral program
"""
import turtle as t

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t.speed('fastest')

for x in range(360):
    t.pencolor(colors[x % 6])
    t. width(x / 100 + 1)
    t.forward(x)
    t.left(59)

t.mainloop()