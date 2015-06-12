'''
Created on 16.06.2015

@author: kolbe
'''
from cberry import CBerry
import time

if __name__ == '__main__':
    display = CBerry()
    display.drawImage("Wiki-background.jpeg")
    time.sleep(2)
    display.drawImage("nyan.jpg")
    display.release()
    
    
    