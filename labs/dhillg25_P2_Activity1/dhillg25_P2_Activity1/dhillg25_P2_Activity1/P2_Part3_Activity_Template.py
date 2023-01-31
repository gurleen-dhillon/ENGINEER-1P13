'''
DP-2 Activity (Part 3 - Interfacing Muscle Sensor Emulator and Turtle Graphics)
'''

## Import the MuscleGUILib, turtle, and time modules
from MuscleGUILib import *
import turtle
import time

'''
Initialize an object of EMGSim() from the MuscleGUILib module
'''
## Write code below this line
emg = EMGSim()

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
Define variables that correspond to your thresholds for moving the turtle graphic
1. Refer to Activity Instructions
'''
## Write code below this line
thres = 0.3
bob.speed(1)

'''
Write a program for controlling turtle movements using continuous input from the muscle emulator
'''
## Write code below this line
while True:
    emg.update()
    print("Left:", emg.myoL, "Right:", emg.myoR)
    time.sleep(0.25)


    if emg.myoL>thres:
        bob.forward(emg.myoL*30)
        

    if emg.myoR>thres:
        bob.right(10)


    if emg.myoL>thres and emg.myoR>thres:
        bob.right(10)
        bob.forward(emg.myoL*30)

