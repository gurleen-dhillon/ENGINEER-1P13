'''
DP-2 Activity (Part 2 - Muscle Sensor Emulator)
Output: Display the muscle sensor value every 0.5 seconds
'''

## Import the MuscleGUILib and time modules
from MuscleGUILib import *
import time

## Initialize an object of EMGSim() from the MuscleGUILib module
emg = EMGSim()

'''
Translate the pseudocode below, shown in paired-quotations
Make sure you write your code OUTSIDE the paired-quotations (otherwise Python will ignore it)
'''
## Each line below is pseudocode for ONE LINE of code in your program
'''
Initiate an infinite loop
    Update the emg readings
    Display the updated emg reading for the left and right myo sensors
    Pause the program for 0.25 seconds
'''
## Write code below this line
while True:
    emg.update()
    print("left", emg.myoL)
    print("right", emg.myoR)
    time.sleep(0.25)

