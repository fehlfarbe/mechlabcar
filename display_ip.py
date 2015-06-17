'''
Created on 17.06.2015

@author: kolbe
'''
from cberry import CBerry
import socket

if __name__ == '__main__':
    display = CBerry()
    while True:
        try:
            ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
            break
        except:
            pass
    print ip
    display.drawString(0, 0, "IP: %s" % ip)
    display.release()