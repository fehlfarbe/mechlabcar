'''
Created on 17.06.2015

@author: kolbe
'''
import time
import datetime

from cberry import CBerry
from can import TinyCAN
from car import Car

if __name__ == '__main__':
    
    print "mechlabcar main program"
    
    ### init cberry display
    display = CBerry()
    ### init CAN interface
    can = TinyCAN()
    can.connect()
    ### init car
    car = Car()
    ### init camera
    # ToDo
    
    while True:
        ### read can messages and print to display
        messages = can.recieveMessages()
        for i,msg in enumerate(messages):
            display.drawString(0, i*20, "%s %s" %(datetime.datetime.now().strftime("%H:%m:%S"), msg))
            print msg
            
        ### read car values
        speed = car.speed
        light_angle = car.light.angle
        print speed, light_angle
            
        time.sleep(0.1)
        
    ### cleanup
    display.release()
    can.disconnect()
    
    