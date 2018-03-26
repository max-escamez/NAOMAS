# -*- encoding: UTF-8 -*-

"""
Main.
"""

import time
import argparse
import numpy as np
from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker


def intention(tracker, tts, target, motion, posture, bdi):
    if not tracker.isTargetLost():
        tts.say("Je vois quelqu'un")
        
        #Find the caracteristiques of the person
        target = tracker.getTargetPosition()
        phi = np.arctan2(target[1], target[0])
        # todo : récupérer l'identifiant de la personne détectée        
        # Todo : add the person to the believes : bdi['identifiant'] = {x , y} si la personne n'y est pas déjà
        
        
        # Todo : move to the person that correspond to the believes or the best person founded in the believes
        # move close to the person
        if target[1]-offset > 0:
            motion.moveTo(target[0]+offset, target[1]-offset, phi)
            tts.say("J'ai quelque chose à te dire")
        else :
            tts.say("J'ai quelque chose à te dire et je n'ai même pas eu à bouger")
    else:
        tts.say("Je ne vois personne")

# Il faudrait vérifier mais pour moi on a pas besoin de ces deux affectations ...
# ReactToTouch = None
# memory = None

def main(IP, PORT, faceSize):
    
    # Brocker
    print "Connecting to", IP, "with port", PORT
    motion = ALProxy("ALMotion", IP, PORT)
    tracker = ALProxy("ALTracker", IP, PORT)
    posture = ALProxy("ALRobotPosture", IP, PORT)
    tts = ALProxy("ALTextToSpeech",IP, PORT)
    
    reactToTouch = ALProxy("ReactToTouch", IP, PORT)
    # au lieu de : global ReactToTouch
    # et : ReactToTouch = ReactToTouch("ReactToTouch")

    myBroker = ALBroker("myBroker","0.0.0.0",  # listen to anyone
                        0,  # find a free port and use it
                        IP,  # parent broker IP
                        PORT)
                        
    # the mental representation of the robot :
    bdi = BDI(Desire(True))

    motion.wakeUp()
    posture.goToPosture("Stand", 1.0)

    # Add target to track.
    targetName = "Face"
    faceWidth = faceSize
    offset = 0.10
    tracker.registerTarget(targetName, faceWidth)


    # Then, start tracker.
    tracker.track(targetName)

    print "ALTracker successfully started, now show your face to robot!"
    print "Use Ctrl+c to stop this script."

    flag = True
    try:
        while True:
            time.sleep(1)
            if True:
                moveToPeople(tracker, tts, target, motion, posture, bdi)
                posture.goToPosture("Sit", 1.0)
                flag = False
            else:
                tts.say("Je suis déjà assez prêt de toi wesh")

    except RuntimeError, e:
        print e
        exit(1)

    except KeyboardInterrupt:
        print "Interrupted by user"
        posture.goToPosture("Sit", 1.0)
        exit(2)

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