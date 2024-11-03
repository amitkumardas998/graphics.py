import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the speed to the fastest
pen.width(2)  # Set the pen width

colors = ["red", "yellow", "blue", "green", "orange", "purple"]

# Draw a spiral
for i in range(360):
    pen.color(colors[i % 6])  # Cycle through the colors
    pen.forward(i)
    pen.left(59)  # Turn left by 59 degrees

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()