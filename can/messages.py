'''
Created on 22.06.2015

@author: kolbe
'''

can_messages = {
    'LIGHT' : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    'LIGHT_DIRECTION' : [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    
}


def getCanMessage(msg_name, active=False):
    return can_messages[msg_name]

def getMessageName(msg):
    for key in can_messages:
        if msg == can_messages[key]:
            return key
        
    return None
        
        
if __name__ == '__main__':
    print getMessageName([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    