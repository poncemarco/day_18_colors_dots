import turtle as t
import random

# tim = t.Turtle()
# tim.shape('turtle')
# tim.color('coral2')
#pen = t.Turtle()
#Poner el formato r,g,b y hacer colores al azar
#t.colormode(255)
#pen.pensize(15)
#pen.speed("fastest")

#colors = ['red', 'blue', 'coral', 'coral3', 'green', 'pink', 'brown', 'black', 'yellow', 'blue3', 'purple',
          #'navajo white', 'sandy brown','orange','chocolate','maroon','light salmon','tomato']
#Elegir un color al azar sin lista:
#Python Tuples
"""Son variables inmutables, no pueden ser cambiadas"""
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

dir = [0,90,180,270]

# Nota: Se pueden instalar usando esto: se lecciona cuando este en rojo y lo instala
# import heroes

# print(heroes.gen())
#


# Movimiento
# for _ in range(15):
#    tim.fd(10)
#   tim.penup()
#  tim.fd(10)
# tim.pendown()

"""Se busca un programa que dibuje poligonos desde 3 lados a 12 lados """
#while on:
    #for lados in range(3, 13):
        #pen.color(random.choice(colors))
        #for j in range(lados):
            #pen.fd(50)
            #pen.right(360 / (lados))


"""Se busca que la tortuga haga un movimiento aleatorio"""
#for i in range(200):
    #pen.color(random_color())
    #pen.forward(100)
    #pen.setheading(random.choice(dir))

# TODO create a screen and the way to end it
#screen = t.Screen()
#screen.exitonclick()
