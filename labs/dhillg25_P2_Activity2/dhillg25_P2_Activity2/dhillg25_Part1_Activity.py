'''
DP-2 Activity (Part 1 - Determine xyz coordinates for cube and sphere pick-up location)
- Commands are meant to be typed in the Python Shell
'''

import time
import sys
sys.path.append('../')

from Common_Libraries.p2_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim ():
    try:
        arm.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

arm = qarm()

update_thread = repeating_timer(2, update_sim)
## *******************************************
## DO NOT EDIT ANY OF THE CODE ABOVE THIS LINE
## *******************************************


'''
Determine xyz coordinates for CUBE pick-up location
1. Run the module in the Python Shell
2. Move Qarm to pick up CUBE, typing commands in the Python Shell
3. Write down CUBE pick-up location xyz coordinates for future use

XYZ COORDINATES FOR CUBE: (0.6864, 0.0, 0.3317)
'''

#code to go to cube
"""
arm.home()
time.sleep(5)
arm.rotate_shoulder(52)  
arm.rotate_elbow(-50)
arm.control_gripper(45)
arm.effector_position()
"""

'''
Determine xyz coordinates for SPHERE pick-up location
1. Run the module in the Python Shell
2. Move Qarm to pick up SPHERE, typing commands in the Python Shell
3. Write down SPHERE pick-up location xyz coordinates for future use

XYZ COORDINATES FOR SPHERE:(0.3648, -0.3648, 0.2866)
'''

#code to go to sphere
"""
arm.home()
time.sleep(5)
arm.rotate_base(-45)
arm.rotate_shoulder(24)
arm.control_gripper(45)
arm.effector_position()
"""

## All commands should be typed directly in the Python Shell
## DO NOT WRITE any code below this line

