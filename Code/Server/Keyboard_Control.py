#!/usr/bin/python3
#Import everything in the control module, 
#including functions, classes, variables, and more.
from Control import *
import keyboard
import time
import cv2
import Led
import ADS7830

# Creating object 'control' of 'Control' class.
c=Control()

# Create LED controller
led=Led.Led()

def battery_volt_to_RGB(v):
    # >8V is green
    # 8..7V is becomming yellow
    # 7..6V is becomming red
    # 6..5V is becoming blue
    if v>=8:
        return (0,255,0)
    elif v>=7:
        d = v-7
        return (int(255*(1-d)),255,0)
    elif v>=6:
        d = v-6
        return (255,int(255*d),0)
    elif v>=5:
        d = v-5
        return (int(255*d),0,int(255*(1-d)))
    else:
        return (0,0,0)


# Create Power ADC controller
adc = ADS7830.ADS7830()

# Create camera objects
def init_camera(index):
    cam = cv2.VideoCapture(index)
    if not cam.isOpened():
        print("Error opening camera", index)
        exit(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cam.set(cv2.CAP_PROP_FPS , 15)
    return cam

camL = init_camera(0)
camR = init_camera(2)

# grab a few frames to make auto exposure correct
for _ in range(1,15):
    camL.grab()
    camR.grab()

print("Ready for input")

# Current camera frame index
frame_index = 0
frame_file_name_format = '/home/pi/capture/{0:04d}_{1}.jpg'

# Attiture angles
roll = pitch = yaw = 0
# Body positions
body_x = body_y = body_z = 0

while True:
    capture = True
    if keyboard.is_pressed('esc'):
        # Stand on all legs
        data=['CMD_MOVE', '1', '0', '0', '10', '0']
        c.run(data)
        # Motor power off
        c.relax(True)
        break

    # Stand

    elif keyboard.is_pressed('d'):
        #Stand on all legs
        data=['CMD_MOVE', '1', '0', '0', '10', '0']
        c.run(data)
        # The above command resets roll itch yaw and body pos
        roll = pitch = yaw = 0
        body_x = body_y = body_z = 0

    elif keyboard.is_pressed('p'):
        #Stand on all legs, then relax
        data=['CMD_MOVE', '1', '0', '0', '10', '0']
        c.run(data)
        # Motor power off
        c.relax(True)

    # Usual "walk and turn" action

    elif keyboard.is_pressed('e'):
        #Move forward
        data=['CMD_MOVE', '1', '0', '35', '10', '0']
        c.run(data)

    elif keyboard.is_pressed('w'):
        #Move forward turning left
        data=['CMD_MOVE', '1', '0', '35', '10', '-10']
        c.run(data)

    elif keyboard.is_pressed('r'):
        #Move forward turning right
        data=['CMD_MOVE', '1', '0', '35', '10', '10']
        c.run(data)

    elif keyboard.is_pressed('c'):
        #Move backward
        data=['CMD_MOVE', '1', '0', '-35', '10', '0']
        c.run(data)

    elif keyboard.is_pressed('x'):
        #Move backward turning left
        data=['CMD_MOVE', '1', '0', '-35', '10', '10']
        c.run(data)

    elif keyboard.is_pressed('v'):
        #Move backward turning right
        data=['CMD_MOVE', '1', '0', '-35', '10', '-10']
        c.run(data)

    elif keyboard.is_pressed('s'):
        #Spot turn left
        data=['CMD_MOVE', '1', '0', '0', '10', '-10']
        c.run(data)

    elif keyboard.is_pressed('f'):
        #Spot turn right
        data=['CMD_MOVE', '1', '0', '0', '10', '10']
        c.run(data)

    # Sideways walks

    elif keyboard.is_pressed('a'):
        #Move left sideways
        data=['CMD_MOVE', '1', '-35', '0', '10', '0']
        c.run(data)

    elif keyboard.is_pressed('q'):
        #Move front left without turn
        data=['CMD_MOVE', '1', '-25', '25', '10', '0']
        c.run(data)

    # Note: y is for german keyboards
    elif keyboard.is_pressed('y'):
        #Move backwards left without turn
        data=['CMD_MOVE', '1', '-25', '-25', '10', '0']
        c.run(data)

    elif keyboard.is_pressed('g'):
        #Move right sideways
        data=['CMD_MOVE', '1', '35', '0', '10', '0']
        c.run(data)

    elif keyboard.is_pressed('t'):
        #Move front right without turn
        data=['CMD_MOVE', '1', '25', '25', '10', '0']
        c.run(data)

    elif keyboard.is_pressed('b'):
        #Move backwards right without turn
        data=['CMD_MOVE', '1', '25', '-25', '10', '0']
        c.run(data)

    # Attitude commands

    elif keyboard.is_pressed('z'):
        roll -= 1
        c.attitude(roll, pitch, yaw)
        time.sleep(0.1)

    elif keyboard.is_pressed('u'):
        roll += 1
        c.attitude(roll, pitch, yaw)
        time.sleep(0.1)

    elif keyboard.is_pressed('h'):
        pitch -= 1
        c.attitude(roll, pitch, yaw)
        time.sleep(0.1)

    elif keyboard.is_pressed('j'):
        pitch += 1
        c.attitude(roll, pitch, yaw)
        time.sleep(0.1)

    elif keyboard.is_pressed('n'):
        yaw -= 1
        c.attitude(roll, pitch, yaw)
        time.sleep(0.1)

    elif keyboard.is_pressed('m'):
        yaw += 1
        c.attitude(roll, pitch, yaw)
        time.sleep(0.1)

    # Position commands

    elif keyboard.is_pressed('i'):
        body_x -= 2
        c.position(body_x, body_y, body_z)
        time.sleep(0.1)

    elif keyboard.is_pressed('o'):
        body_x += 2
        c.position(body_x, body_y, body_z)
        time.sleep(0.1)

    elif keyboard.is_pressed('k'):
        body_y -= 2
        c.position(body_x, body_y, body_z)
        time.sleep(0.1)

    elif keyboard.is_pressed('l'):
        body_y += 2
        c.position(body_x, body_y, body_z)
        time.sleep(0.1)

    elif keyboard.is_pressed(','):
        body_z -= 2
        c.position(body_x, body_y, body_z)
        time.sleep(0.1)

    elif keyboard.is_pressed('.'):
        body_z += 2
        c.position(body_x, body_y, body_z)
        time.sleep(0.1)
    
    else:
        capture = False

   
    if(capture):
        # Get battery power
        power = adc.batteryPower()
        rgb1 = battery_volt_to_RGB(power[0])
        rgb2 = battery_volt_to_RGB(power[1])
        # Flash LED with battery status
        led.strip.setPixelColorRGB(2,rgb1[0],rgb1[1],rgb1[2])
        led.strip.setPixelColorRGB(4,rgb2[0],rgb2[1],rgb2[2])
        led.strip.show()

        frame_index += 1
        camL.grab()
        camR.grab()
        retL, frameL = camL.retrieve()
        retR, frameR = camR.retrieve()
        if retL:
            cv2.imwrite(frame_file_name_format.format(frame_index,"L"),frameL)
        if retR:
            cv2.imwrite(frame_file_name_format.format(frame_index,"R"),frameR)

        # Flash LED with battery status
        led.strip.setPixelColorRGB(2,0,0,0)
        led.strip.setPixelColorRGB(4,0,0,0)
        led.strip.show()
