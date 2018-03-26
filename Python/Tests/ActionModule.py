# faire avancer nao

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import math

class ActionModule(ALModule):
    """ A simple module able to move toward an object and take or leave it"""
    
    def __init__(self, name):
        """Constructor"""
        ALModule.__init__(self, name, ip, port)
        self.nao_ip = ip
        self.nao_port = port
        
    def moveTowardObject(x, y, rotation):
        """Move toward an object or the goal"""
        motion_proxy = ALProxy('ALMotion', self.nao_ip, self.nao_port)
        motion_proxy.wakeUp()
        if (rotation != 0):
            # make the rotation
            motion_proxy.moveTo(0, 0, rotation)
        # move forward
        motion_proxy.moveTo(x, y, 0)
    
    def takeObject(x, y, rotation):
        """Take an object"""
        # TODO : prendre l'objet
        pass   
        
    def dropObject(x, y, rotation):
        """Drop the object"""
        # TODO : lacher l'objet
        pass