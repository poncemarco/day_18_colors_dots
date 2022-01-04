"""Proyecto del día:
Usar documentación y conocimientos previos para hacer un cuadro con los colores extraidos
de 10 x 10 con puntos 20 of size  """
import colorgram
import random
import turtle as t
from random_movement import random_color



t.colormode(255)
dot =t.Turtle()
dot.penup()
dot.hideturtle()
dot.speed('fastest')




dot.setheading(225)
dot.forward(300)
dot.setheading(0)
number_of_dots = 100



#Obtener los colores
rgb_colors = []
colors = colorgram.extract('image.jpg',16)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)


#Definir el patrón de impresión de circulo

#def print_line():
    #for _ in range(10):
        #dot.color(random.choice(rgb_colors))
        #dot.dot(20, random.choice(rgb_colors))
        #dot.forward(50)
    #dot.pendown()


for dot_count in range(1,number_of_dots+1):
    dot.dot(20, random.choice(rgb_colors))
    dot.forward(50)


    if dot_count % 10 == 0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)



#Crear una pantalla
screen = t.Screen()
screen.exitonclick()











