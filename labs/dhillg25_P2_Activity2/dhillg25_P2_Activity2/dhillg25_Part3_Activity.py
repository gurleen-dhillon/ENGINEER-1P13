'''
DP-2 Activity (Part 3 - Pick up and drop off 1 cylinder, 1 cube and 1 sphere)
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
Define a list for each location (e.g., cylinder pick-up, cylinder drop-off, etc.)
'''
## Write code below this line
Sphere_location = [0.3667, -0.3667, 0.2775]
Sphere_Dropoff = [-0.3935, 0.2755, 0.4748]
cylinder_location = [0.5235,0.2331,0.4552]
cylinder_Dropoff = [0.0314,-0.4486,0.487]
Cube_location = [0.6977, 0, 0.331]
Cube_Dropoff = [-0.4351, -0.2029, 0.4606]

'''
Define a list for the 3 pick-up locations
Define a list for the 3 drop-off locations
'''
## Write code below this line
pickup = [cylinder_location, Cube_location, Sphere_location]
dropoff = [cylinder_Dropoff, Cube_Dropoff, Sphere_Dropoff]

'''
Pick up and drop off 1 cylinder, 1 cube and 1 sphere
'''
## Write code below this line
for i in range (3):
    arm.move_arm(pickup[i][0], pickup[i][1], pickup[i][2])
    time.sleep(2)
    arm.control_gripper(45)
    time.sleep(2)
    arm.move_arm(0.4064,0,0.4826)
    time.sleep(2)
    arm.move_arm(dropoff[i][0],dropoff[i][1],dropoff[i][2])
    time.sleep(2)
    arm.control_gripper(-45)
    time.sleep(2)
    arm.move_arm(0.4064,0,0.4826)
    time.sleep(2)
    arm.home()
    

