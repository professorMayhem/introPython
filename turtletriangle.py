import turtle

# Create the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Optional: make the turtle move faster
t.speed(3)

# Draw an equilateral triangle
for _ in range(3):
    t.forward(150)   # length of each side
    t.left(120)      # exterior angle for equilateral triangle

# Keep the window open until clicked

t.up()
t.goto(-100, -100)
t.write("Click HERE to close the window")
screen.exitonclick()
