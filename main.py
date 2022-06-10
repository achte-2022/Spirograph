#Importing Libraries
import turtle
import random

#Constants
MAX_INTENSITY = 255
ANGLES = [0, 90, 180, 270]
RADIUS = 100
NUM_CIRCLES = 72
SPEED = 'fastest'
SHAPE = 'classic'
BG_COLOR = 'black'

#Color Setup
turtle.colormode(MAX_INTENSITY)

#Generate Random Color
def random_color():
    red = random.randint(0, MAX_INTENSITY)
    green = random.randint(0, MAX_INTENSITY)
    blue = random.randint(0, MAX_INTENSITY)
    return (red, green, blue)

#Draw Spirograph
def draw_spirograph(turtle_object, radius, num_circles):
    if num_circles > 360:
        num_circles = 18
    tilt_angle = 360 / num_circles
    for i in range(num_circles):
        color = random_color()
        turtle_object.color(color)
        turtle_object.left(tilt_angle)
        turtle_object.circle(radius)
    return

#Object Setup
window = turtle.Screen()
window.bgcolor(BG_COLOR)
turtle_object = turtle.Turtle()
turtle_object.shape(SHAPE)
turtle_object.speed(SPEED)

draw_spirograph(turtle_object, RADIUS, NUM_CIRCLES)
turtle_object.hideturtle()

window.exitonclick()
