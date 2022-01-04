#Make a Spirograph
import turtle as t
import random
from random_movement import random_color
circle = t.Turtle()
t.colormode(255)
circle.speed('fastest')
def mov_circ():
    circle.circle(50)
    circle.color(random_color())


for _ in range(360):
    mov_circ()
    circle.right(_)



screen = t.Screen()
screen.exitonclick()