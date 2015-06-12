import os
from ctypes import *
from PIL import Image
import numpy as np

basepath = os.path.split(os.path.abspath(__file__))[0]
print basepath

class CBerry(object):
    
    lib = None
    display_size = (320, 240)
    
    def __init__(self):
        self.lib = cdll.LoadLibrary(os.path.join(basepath, "./libcberry.so"))
        #print self.lib
        self.lib.init()
        
    def drawBuffer(self, buf):
        self.lib.loadBuffer(c_char_p(buf))
        
    def drawImage(self, filename):
        img = Image.open(filename)
        img.thumbnail((320, 240), Image.ANTIALIAS)
        self.drawBuffer(np.array(img).tostring())
        
    def release(self):
        self.lib.release()