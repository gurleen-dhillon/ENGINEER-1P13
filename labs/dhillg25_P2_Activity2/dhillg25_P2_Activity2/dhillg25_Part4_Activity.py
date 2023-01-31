'''
DP-2 Activity (Part 4a - Write a program for transferring shapes based on user input)
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
Define a function get_pickup() that returns the pick-up location for a shape
- You can copy-and-paste your solution from Demo #4
'''
## Write your function below this line
def get_pickup(i):
    if i == 1:     #cylinder
        pickup = [0.5235,0.2331,0.4552]
    elif i == 2:   #cube
        pickup = [0.6977, 0.0, 0.331]
    elif i == 3:   #sphere
        pickup = [0.3667, -0.3667, 0.2775] 
    else:
        print("invalid input")
        pickup = [0.4064,0,0.4826]
    return pickup

'''
Define a function get_dropoff() that returns the drop-off location for a shape
'''
## Write your function below this line
def get_dropoff(i):
    if i == 1:     #cylinder
        dropoff = [0.0314,-0.4486,0.487]
    elif i == 2:   #cube
        dropoff = [-0.4351, -0.2029, 0.4606]
    elif i == 3:   #sphere
        dropoff = [-0.3935, 0.2755, 0.4748]
    else:
        print("invalid input")
        dropoff = [0.4064,0,0.4826]
    return dropoff

'''
Define a function pick_up() that picks up an object from an input location
'''
## Write your function below this line
def Pick_up():
    print("Please input pickup location: ")
    return input()

'''
Define a function drop_off() that drops off an object at an input location
'''
## Write your function below this line
def Drop_Off():
    print("Please input drop-off location: ")
    return input()

'''
PART 1 - Define an infinite loop for picking up objects based on user input
'''
## Write code below this line
while True:
    x = Pick_up()
    y = Drop_Off()

    Pick_up = get_pickup(int(x))
    Drop_Off = get_dropoff(int(y))

    arm.move_arm(Pick_up[0],Pick_up[1],Pick_up[2])
    time.sleep(2)
    arm.control_gripper(45)
    time.sleep(2)
    arm.move_arm(0.4064,0,0.4826)
    time.sleep(2)
    arm.move_arm(Drop_Off[0],Drop_Off[1],Drop_Off[2])
    time.sleep(2)
    arm.control_gripper(-45)
    time.sleep(2)
    arm.move_arm(0.4064,0,0.4826)
    time.sleep(2)




    




