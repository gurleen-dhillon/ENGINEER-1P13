import time
import random
import sys
sys.path.append('../')

from Common_Libraries.p3b_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim():
    try:
        my_table.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

### Constants
speed = 0.2 #Qbot's speed

### Initialize the QuanserSim Environment
my_table = servo_table()
arm = qarm()
arm.home()
bot = qbot(speed)

##---------------------------------------------------------------------------------------
## STUDENT CODE BEGINS
##---------------------------------------------------------------------------------------

'''
Team: Mon-32
Computing Sub-team: Juliana Konstantinou (konstanj)
                    and Gurleen Dhillon (dhillg25)

'''

'''
CONFIGURATION SETTINGS
    TABLE
        short tower angle = 270
        tall tower angle = 0
        drop tube angle = 180
        
    QBOT
        orientation after reset = 180
        location along line after reset = 0
        camera angle = -21.5
        all display options on
        
    ENVIRONMENT
        all offset = 55
        metallic off
        roughness = 0.5
        all lines = red 1 and green 0.5
        box 1 = all 0
        box 2 = red 1
        box 3 = blue 1
        box 4 = green 1

    BOX
        width = 33.8
        length = 22.7
        wall height (clockwise starting at top) = 10, 1, 7, 10
        x = -2
        y = 0
        z = 27
'''




def drop_container():
    #Coded by Gurleen Dhillon
    '''
    Function: drop_container()
    Purpose: dispense a random bottle and finds it's attributes
    Input: N/A
    Output: mass of container and destination bin id of container    
    '''
    bottle = random.randint(1,6) #gives a random number for the container
    properties = my_table.container_properties(bottle)
    my_table.dispense_container()
    mass = properties [1]
    bin_id = properties [2]
    time.sleep(0.5)
    return mass, bin_id




def load_container(mass, bin_id):
    #Coded by Gurleen Dhillon
    '''
    Function: load_container()
    Purpose: puts first container on q-bot and determines if other ...
             ...containers should be placed
    Input: takes in the inputs of the mass and bin id of the container dropped
    Output: will output the bin id of the 1st container...
            and the mass and bin id the of newer dropped container 
    '''
    p = 2
    og_bin_id = "N/A"
    tot_mass = mass
    og_bin_id = bin_id
    pickup(1)
    print("bin destination:", og_bin_id)
    print("total mass on q-bot = ", tot_mass)
    new_mass = 0
    new_bin_id = "N/A"
    
    for i in range (1,4):
        if p == 2:
            mass, bin_id = drop_container()
            if og_bin_id == bin_id:
                if (tot_mass + mass) < 90:
                    tot_mass = tot_mass + mass
                    pickup(2)
                    p = 3
                    print("total mass on q-bot = ", tot_mass)
                else:
                    new_mass = mass
                    new_bin_id = bin_id
                    break
            else:
                new_mass = mass
                new_bin_id = bin_id
                break
        elif p == 3:
            mass, bin_id = drop_container()
            if og_bin_id == bin_id:
                if (tot_mass + mass) < 90:
                    tot_mass = tot_mass + mass
                    pickup(3)
                    print("total mass on q-bot = ", tot_mass)
                    new_mass, new_bin_id = drop_container()
                else:
                    new_mass = mass
                    new_bin_id = bin_id
                    break
            else:
                new_mass = mass
                new_bin_id = bin_id
                break
        else:
            break
    return og_bin_id, new_mass, new_bin_id  




def pickup(pickup_num):
    #Coded by Gurleen Dhillon
    '''
    Function: pickup()
    Purpose: to get q-arm to pick up container and drop it in q-bot
    Input: number of bottles that have been picked up
    Output: N/A
    '''
    #the number of pickups already done determine where the container...
    #...will be placed on q-bot
    if pickup_num == 2:
        bottle = -64
    elif pickup_num == 3:
        bottle = -50
    else:
        bottle = -80
    #q-arm transfers container to q-bot
    arm.home()
    arm.rotate_shoulder(45)
    arm.rotate_elbow(-30)
    arm.control_gripper(32)
    arm.rotate_elbow(-3)
    arm.rotate_base(-25)
    arm.rotate_shoulder(-45)
    arm.rotate_base(bottle)
    arm.rotate_shoulder(-10)
    arm.rotate_elbow(50)
    arm.control_gripper(-5)
    arm.rotate_shoulder(-35)




def transfer_container(bin_id):
    #Coded by Juliana Konstantinou
    '''
    Function: transfer_container()
    Purpose: to get q-bot to go to correct bin
    Input: the bin id of the container we are transfering
    Output: no output
    '''    
    #bot will move forward so it is in line with first bin, if it is not...
    #...metal then it with test the other bins
    if bin_id == "Bin01":
        #Bin01 is black and is for metal containers
        bot.forward_time(4.4)
    elif bin_id == "Bin02":
        #Bin02 is red and is for paper
        bot.forward_time(4.4)
        bot.activate_color_sensor("Red")
        for i in range(3):
            #will check each bin that it stops beside to detect red
            sensor_readings = bot.read_red_color_sensor("Bin02",0.6)
            sensor_avg = (sensor_readings[0] + sensor_readings[1] + sensor_readings[2])/3
            if sensor_avg >= 4.6:
                bot.stop()
                break
            else:
                #when red is not detected at a bin, the bot will continue...
                #...forward to check the next bin
                bot.forward_time(1.8)
        bot.deactivate_color_sensor()
    elif bin_id == "Bin03":
        #Bin03 is blue and is for plastic
        bot.forward_time(4.4)
        bot.activate_color_sensor("Blue")
        for i in range(3):
            #will check each bin that it stops beside to detect blue
            sensor_readings = bot.read_blue_color_sensor("Bin03",0.6)
            sensor_avg = (sensor_readings[0] + sensor_readings[1] + sensor_readings[2])/3
            if sensor_avg >= 4.6:
                bot.stop()
                break
            else:
                #when blue is not detected at a bin, the bot will continue...
                #...forward to check the next bin
                bot.forward_time(1.8)
        bot.deactivate_color_sensor()
    elif bin_id == "Bin04":
        #Bin04 is green and is for garbage 
        bot.forward_time(4.4)
        bot.activate_color_sensor("Green")
        for i in range(3):
            #will check each bin that it stops beside to detect green
            sensor_readings = bot.read_green_color_sensor("Bin04",0.6)
            sensor_avg = (sensor_readings[0] + sensor_readings[1] + sensor_readings[2])/3
            if sensor_avg >= 4.6:
                bot.stop()
                break
            else:
                #when green is not detected at a bin, the bot will continue...
                #...forward to check the next bin
                bot.forward_time(1.8)
        bot.deactivate_color_sensor()
    else:
        bot.stop()




def deposit_container():
    #Coded by Juliana Konstantinou
    '''
    Function: depostit_container()
    Purpose: to get q-bot to empty out tray into destination bin
    Input: no inputs
    Output: no outputs
    '''
    #turn qbot so it is heading toward the bin
    bot.rotate(93)
    time.sleep(1)
    bot.forward_time(2.3)
    time.sleep(1)
    #turn qbot so when we lift the box, the container will dump into the bin
    bot.rotate(-91)
    time.sleep(1)
    #dump containers into bin
    bot.activate_actuator()
    bot.dump()
    bot.deactivate_actuator()
    time.sleep(1)
    #go back to the main yellow line
    bot.rotate(-91)
    time.sleep(1)
    bot.forward_time(2.3)
    time.sleep(1)
    bot.rotate(91)




def return_home():
    #Coded by Juliana Konstantinou
    '''
    Function: return_home()
    Purpose: to get q-bot to return home
    Input: no inputs
    Output: no outputs
    '''
    #follow yellow line back to the home position
    num_line = 0
    while num_line < 2:
        num_line, velocity = bot.follow_line(0.3)
        bot.forward_velocity(velocity)
    bot.stop()
    bot.forward_time(0.5)
    #turn around
    bot.rotate(189.5)




def main():
    #Coded by Gurleen Dhillon
    '''
    Function: main()
    Purpose: to combine all functions together so the system runs property
    Input: no inputs
    Output: no outputs
    '''
    #for first dispening round
    mass, bin_id = drop_container()
    i = 1
    #go through loop infite number of times
    while i == 1:
        #take in last dipensed bottle's bin_id and mass to be used in next loop
        og_bin_id, mass, bin_id = load_container(mass, bin_id)
        #tranfer bottle and go home
        transfer_container(og_bin_id)
        deposit_container()
        return_home()
        

main()


##---------------------------------------------------------------------------------------
## STUDENT CODE ENDS
##---------------------------------------------------------------------------------------
update_thread = repeating_timer(2,update_sim)

