# -*- encoding: UTF-8 -*-

"""
React to touch.
"""

import time
import argparse
import numpy as np
from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker


# Todo : A vérifier mais je ne pense pas qu'on ait besoin de ces deux initalisations :
ReactToTouch = None
memory = None

class ReactToTouch(ALModule):
    """ A simple module able to react
        to touch events.
    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        self.posture = ALProxy("ALRobotPosture")

        global memory
        memory = ALProxy("ALMemory")
        # TODO : remplacer TouchChanged par FrontTactilTouched pour ne réagir que en cas de front touché
        memory.subscribeToEvent("TouchChanged", "ReactToTouch", "onTouched")

    def onTouched(self, strVarName, value):
        # TODO : remplacer TouchChanged par FrontTactilTouched pour ne réagir que en cas de front touché
        memory.unsubscribeToEvent("TouchChanged", "ReactToTouch")
        for p in value:
            if p[0] == 'Head' and p[1]:
                self.posture.goToPosture("Crouch", 1.0)
        # TODO : remplacer TouchChanged par FrontTactilTouched pour ne réagir que en cas de front touché
        memory.subscribeToEvent("TouchChanged", "ReactToTouch", "onTouched")