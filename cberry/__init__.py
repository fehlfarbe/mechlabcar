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
        self.lib.init()
        
    def drawBuffer(self, buf):
        self.lib.loadBuffer(c_char_p(buf))
        
    def drawImage(self, filename):
        img = Image.open(filename)
        img.thumbnail(self.display_size, Image.ANTIALIAS)
        self.drawBuffer(np.array(img).tostring())
        
    def drawString(self, x, y, text, bg_color=0, fg_color=255):
        self.lib.drawString(x, y, text, bg_color, fg_color)
        
    def release(self):
        self.lib.release()