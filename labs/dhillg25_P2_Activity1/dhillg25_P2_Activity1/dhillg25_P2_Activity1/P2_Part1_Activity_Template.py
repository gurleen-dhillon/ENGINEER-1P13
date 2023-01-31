'''
DP-2 Activity (Part 1 - Turtle Graphics)
'''

'''
Import the turtle module
'''
## Write code below this line
import turtle
import time

'''
Initialize the drawing board
Set the background color to "white"
Title the window "Turtle Graphics"
Set the size of the window to 700x700 pixels
'''
## Write code below this line
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Graphics")
wn.setup(700,700)

'''
Initialize the Turtle graphic
Set the color to "red"
Set the shape to "turtle"
'''
## Write code below this line
bob = turtle.Turtle()
bob.color("red")
bob.shape("turtle")

'''
Sketch out a graphic as instructed on the worksheet
'''
## Write code below this line
bob.speed(1)
bob.forward(120)
bob.right(150)
bob.forward(55)
bob.right(30)
bob.forward(120)
bob.right(150)
bob.forward(55)
bob.right(30)

