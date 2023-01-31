'''
DP-2 Activity (Part 2b - Determine drop-off coordinates for the sphere)
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
Pick up a sphere and return arm to home position
'''
## Write code below this line
arm.home()
time.sleep(2)
arm.move_arm(0.3648, -0.3648, 0.2866)
time.sleep(2)
arm.control_gripper(45)
time.sleep(2)
arm.move_arm(0.4064,0,0.4826)

'''
Determine xyz coordinates of SPHERE drop-off platform
1. Run the module in the Python Shell
2. Move Qarm to drop off SPHERE, typing commands in the Python Shell
3. Write down SPHERE drop-off location xyz coordinates for future use

SPHERE DROP OFF COORDINATES: (-0.3935, 0.2755, 0.4748)
'''
arm.rotate_base(145)
time.sleep(2)
arm.rotate_elbow(-10)
time.sleep(2)
arm.rotate_shoulder(12)
time.sleep(1)
arm.control_gripper(-45)
arm.effector_position()  
time.sleep(1)
arm.home()

## All commands should be typed directly in the Python Shell
## DO NOT WRITE any code below this line


