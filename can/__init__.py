'''
Created on 17.06.2015

@author: kolbe
'''
from abc import ABCMeta, abstractmethod

class AbstractCANBus(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass
    
    @abstractmethod
    def connect(self, bitrate=500, device_nr=None):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def status(self):
        pass
    
    @abstractmethod
    def sendMessage(self, msgId, msgData):
        pass
    
    @abstractmethod
    def recieveMessages(self, filter=None, count=1000):
        pass
    
##################################################
#
# TinyCAN Interface
#
##################################################
import tinycan.mhsTinyCanDriver as CanDriver
    
class TinyCAN(AbstractCANBus):
    
    def __init__(self):
        self.canDriver = CanDriver.MhsTinyCanDriver()

    def connect(self, bitrate=500, device_nr=None):
        err = self.canDriver.OpenComplete(snr=device_nr, canSpeed=bitrate)
        return err
    
    def disconnect(self):
        self.canDriver.CanDownDriver()
        
    def status(self):
        return self.canDriver.CanGetDeviceStatus()
    
    def sendMessage(self, msgId, msgData):
        self.canDriver.TransmitData(0, msgId = msgId, msgData = msgData)
        
    def recieveMessages(self, filter=None, count=1000):
        res = self.canDriver.CanReceive(count = count)
        if res[0] > 0:                 
            msgs = self.canDriver.FormatMessages(res[1])
            return msgs
        else:
            return []