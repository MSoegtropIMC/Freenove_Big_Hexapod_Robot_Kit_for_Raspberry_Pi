#Import everything in the control module, 
#including functions, classes, variables, and more.
from Control import *
import keyboard
import time

#Creating object 'control' of 'Control' class.
c=Control()

#example:
#data=['CMD_MOVE', '1', '0', '25', '10', '0']
#Move command:'CMD_MOVE'
#Gait Mode: "1"
#Moving direction: x='0',y='25'
#Delay:'10'
#Action Mode : '0'   Angleless turn

while True:
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

    elif keyboard.is_pressed('y') or keyboard.is_pressed('z'):
        #Move backwards left without turn
        data=['CMD_MOVE', '1', '-25', '-25', '10', '0']
        c.run(data)

    elif keyboard.is_pressed('y'):
        #Move front right without turn
        data=['CMD_MOVE', '1', '25', '25', '10', '0']
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
