## ----------------------------------------------------------------------------------------------------------
## TEMPLATE
## Please DO NOT change the naming convention within this template. Some changes may
## lead to your program not functioning as intended.

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

import time
import random
## STUDENT CODE BEGINS
## ----------------------------------------------------------------------------------------------------------
## Example to rotate the base: arm.rotateBase(90)

#MON-30
#Qisheng Thomas Wang: wangq157
#Martin Ivanov: ivanom4

#Wrote by Martin
def identify_location(container_id): #provides location for each container drop-off
    if container_id == 1: #small red 
        target_location = [-0.62,0.245,0.3955]
    elif container_id == 2: #small green
        target_location = [0,-0.6578,0.3855]
    elif container_id == 3: #small blue
        target_location = [0,0.6578,0.3855]
    elif container_id == 4: #big red
        target_location = [-0.44,0.16,0.17]
    elif container_id == 5: #big green
        target_location = [0.0, -0.4444,0.156]
    elif container_id == 6: #big blue
        target_location = [0.0, 0.4444,0.156]
    else: #home location
        target_location = [0.4064,0,0.4826]
    return target_location #return coordinates for target location


#Wrote by Thomas
def move_end_effector(target_location, cyclepoint): #moves the robot arm
    threshold = 0
    while True:
        time.sleep(5)
        if arm.emg_left() > threshold and arm.emg_right() == 0: #flex left arm but not right to move arm
            if cyclepoint == "home":
                arm.move_arm(0.4064,0,0.4826) #home location
            elif cyclepoint == "pickup":
                arm.move_arm(0.5304, 0.0, 0.0257) #pickup location
            elif cyclepoint == "dropoff":
                arm.move_arm(target_location[0],target_location[1],target_location[2]) #target location
            break
        else:
            print("Awaiting input from user") #if there is invalid muscle sensor entry, await for correct input


#wrote together
def gripper(cyclepoint): #Open and closes gripper 
    threshold = 0
    while True:
        time.sleep(5)
        if arm.emg_right() > threshold and arm.emg_left() == 0: #flex right arm but not left to control the gripper
            if cyclepoint == "open_gripper": #open gripper at final cycle point to leave container in dropoff location
                arm.control_gripper(-30)
            elif cyclepoint == "close_gripper": #close gripper at beginning cycle point to pick up container
                arm.control_gripper(30)
            break
        else:
            print("Awaiting input from user") #if there is invalid muscle sensor entry, await for correct input


#wrote together
def autoclave(container_id, cyclepoint): #open and closes autoclave drawer
    threshold = 0
    while True:
        time.sleep(5)
        if arm.emg_left() > threshold and arm.emg_right() == arm.emg_left():#flex both arms to equal amounts to open autoclave drawer
            if cyclepoint == "open_autoclave": #open autoclave drawer only if needed (when container ID is 4,5,6)
                if container_id == 4:
                    arm.open_red_autoclave(True)
                elif container_id == 5:
                    arm.open_green_autoclave(True)
                elif container_id == 6:
                    arm.open_blue_autoclave(True)
            elif cyclepoint == "close_autoclaves": #close autoclave drawer otherwise (when container ID is 1,2,3)
                arm.open_red_autoclave(False)
                arm.open_green_autoclave(False)
                arm.open_blue_autoclave(False)
            break
        else:
            print("Awaiting input from user") #if there is invalid muscle sensor entry, await for correct input


#wrote together
def rng(): #randomizes the spawned container
    used = [] #create empty list
    x = random.randint(1,6) #randomly generate a number from 1-6 and that is the container ID
    while len(used) <= 5: #continue this process while there are less than 6 indexes in the list
        if not x in used: #if the random generated nubmer is not in the list, add to list
            used.append(x)
        x = random.randint(1,6) #otherwise, generate another number
    return used


#wrote together
def main(container_id): #runs through one cycle of the program at a time, randomizing the generated container
    time.sleep(5)
    arm.spawn_cage(container_id) #spawn container
    target_location = identify_location(container_id) #identify where to dropoff
    move_end_effector(target_location, "pickup") #move arm to pickup
    gripper("close_gripper") #close gripper to pick up container
    move_end_effector(target_location, "home") #return to home
    if container_id >= 4: #open autoclave if needed
        autoclave(container_id, "open_autoclave")
    move_end_effector(target_location, "dropoff") #move to dropoff location
    gripper("open_gripper") #close gripper to leave container at dropoff location
    move_end_effector(target_location, "home") #return home
    if container_id >= 4: #close autoclave if it was open
        autoclave(container_id, "close_autoclaves")


#wrote together
order = rng() #generate the order for which container spawns
for i in range(6): #loop through all 6 of the containers once, index 0-5
    main(order[i])







