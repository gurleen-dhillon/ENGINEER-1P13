'''
DP-2 Activity (Part 2a - Determine drop-off coordinates for the cube)
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
Pick up a cube and return arm to home position
'''
## Write code below this line
arm.home()
time.sleep(2)
arm.move_arm(0.6977, 0, 0.331)
time.sleep(2)
arm.control_gripper(45)
time.sleep(2)
arm.move_arm(0.4064, 0.0, 0.4826)

'''
Determine xyz coordinates of CUBE drop-off platform
1. Run the module in the Python Shell
2. Move Qarm to drop off CUBE, typing commands in the Python Shell
3. Write down CUBE drop-off location xyz coordinates for future use

CUBE DROP OFF LOCATION:(-0.4351, -0.2029, 0.4606)
'''

#code to drop off cube
"""arm.rotate_base(-155)
time.sleep(2)
arm.rotate_elbow(-12)
time.sleep(2)
arm.rotate_shoulder(12)
time.sleep(2)
arm.effector_position() 
arm.control_gripper(-45)
time.sleep(2)
arm.home()"""

## All commands should be typed directly in the Python Shell
## DO NOT WRITE any code below this line
