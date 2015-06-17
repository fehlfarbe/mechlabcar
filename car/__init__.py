from light import Lightcontrol
from sensors import Sensors

class Car(object):
    
    def __init__(self):
        self.light = Lightcontrol()
        self.sensors = Sensors()
        
    @property
    def speed(self):
        # read speed
        return 0
    
    @speed.setter
    def speed(self, value):
        # set speed
        pass