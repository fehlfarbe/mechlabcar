'''
Created on 17.06.2015

@author: kolbe
'''
import time
import datetime

from cberry import CBerry
from can import TinyCAN

if __name__ == '__main__':
    
    print "mechlabcar main program"
    
    ### init cberry display
    display = CBerry()
    ### init CAN interface
    can = TinyCAN()
    can.connect()
    ### init motors
    # ToDo
    ### init sensors (angle, light, ...)
    # ToDo
    ### init camera
    # ToDo
    
    while True:
        messages = can.recieveMessages()
        for i,msg in enumerate(messages):
            display.drawString(0, i*20, "%s %s" %(datetime.datetime.now().strftime("%H:%m:%S"), msg))
            print msg
        time.sleep(0.1)
        
    ### cleanup
    display.release()
    can.disconnect()
    
    