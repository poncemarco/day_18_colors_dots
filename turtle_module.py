from turtle import Turtle, Screen

#CHALLENGE make a turtle called timmy who draw a square

#TODO create timmy
timmy = Turtle()
timmy.shape('turtle')
timmy.color('blue')

# TODO show the way to draw a circle
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

# TODO create a screen and the way to end it
screen=Screen()
screen.exitonclick()

