# -*- encoding: UTF-8 -*-

"""
This example shows how to use ALTracker with face.
"""

import time
import argparse
import numpy as np
from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker



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
        memory.subscribeToEvent("FrontTactilTouched", "ReactToTouch", "onTouched")

    def onTouched(self, strVarName, value):

        memory.unsubscribeToEvent("FrontTactilTouched", "ReactToTouch")
        #for p in value:
        #    if p[0] == 'Head' and p[1]:
        self.posture.goToPosture("Crouch", 1.0)
        memory.subscribeToEvent("FrontTactilTouched", "ReactToTouch", "onTouched")





def main(IP, PORT, faceSize):

    print "Connecting to", IP, "with port", PORT
    motion = ALProxy("ALMotion", IP, PORT)
    tracker = ALProxy("ALTracker", IP, PORT)
    posture = ALProxy("ALRobotPosture", IP, PORT)
    tts = ALProxy("ALTextToSpeech",IP, PORT)

    myBroker = ALBroker("myBroker","0.0.0.0",  # listen to anyone
                        0,  # find a free port and use it
                        IP,  # parent broker IP
                        PORT)
    global ReactToTouch
    ReactToTouch = ReactToTouch("ReactToTouch")

    #motion.wakeUp()
    #posture.goToPosture("Stand", 1.0)

    # Add target to track.
    targetName = "People"
    peopleid = 1
    faceWidth = faceSize
    offset = 0.10
    tracker.registerTarget(targetName, peopleid)
    print tracker.getRegisteredTargets()

    #mode = "Head"
    #tracker.setMode(mode)

    # Then, start tracker.
    tracker.track(targetName)

    print "ALTracker successfully started, now show your face to robot!"
    print "Use Ctrl+c to stop this script."

    flag = True
    try:
        while flag:
            time.sleep(1)
            if not tracker.isTargetLost():
                tts.say("Je vois quelqu'un")
                target = tracker.getTargetPosition()
                print target[0]
                print target[1]
                print target[2]
                #phi = np.arctan2(target[1], target[0])
                #if target[1]-offset > 0:
                #    motion.moveTo(target[0]+offset, target[1]-offset, phi)
                #    tts.say("J'ai quelque chose à te dire")
                #    posture.goToPosture("Crouch", 1.0)
                #    flag = False
                #else:
                #    tts.say("J'ai quelque chose à te dire et je n'ai même pas eu à bouger")
                #    posture.goToPosture("Crouch", 1.0)
                #    flag = False
            else:
                tts.say("Je ne vois personne")


    except KeyboardInterrupt:
        print "Interrupted by user"
        print "Stopping..."

    # Stop tracker.
    tracker.stopTracker()
    tracker.unregisterAllTargets()
    motion.rest()
    myBroker.shutdown()

    print "ALTracker stopped."


if __name__ == "__main__" :

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.76.111",
                        help="Robot ip address.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number.")
    parser.add_argument("--facesize", type=float, default=0.1,
                        help="Face width.")

    args = parser.parse_args()

    main(args.ip, args.port, args.facesize)