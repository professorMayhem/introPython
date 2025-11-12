#####################################################
#
#   Melissa Holmes
#   Turtle Example for introductory Python courses
#   Fall 2025
#
#####################################################

import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.color("blue")
my_turtle.pensize(3)

for _ in range(4): # Loop four times for four sides
    my_turtle.forward(100)
    my_turtle.left(90)

my_turtle.forward(150)
my_turtle.fillcolor("black")
my_turtle.color("pink")
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()


turtle.done()
