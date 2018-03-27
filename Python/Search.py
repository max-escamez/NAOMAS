#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Mains"""
import qi
import time
import sys
import argparse
from naoqi import ALProxy


class Search(object):
    """
    A simple class to react to face detection events.
    """

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(Search, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("FaceDetected")
        self.subscriber.signal.connect(self.on_human_tracked)
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = session.service("ALTextToSpeech")
        self.face_detection = session.service("ALFaceDetection")
        self.face_detection.subscribe("HumanGreeter")
        self.got_face = False
        self.tracker = session.service("ALTracker")
        self.motion = session.service("ALMotion")


    def on_human_tracked(self, value):
        """
        Callback for event FaceDetected.
        """

        targetname = "Face"
        facewidth = 0.1
        self.tracker.registerTarget(targetname, facewidth)

        if value == []:  # empty value when the face disappears
            self.got_face = False
        elif not self.got_face:  # only speak the first time a face appears
            faceInfoArray = value[1]
            for j in range( len(faceInfoArray)-1 ):
                faceInfo = faceInfoArray[j]
                faceExtraInfo = faceInfo[1]
                if faceExtraInfo[2] == "Max":
                    self.got_face = True
                    self.tracker.track("Face")
                    target = self.tracker.getTargetPosition()
                    print target[0]
                    print target[1]
                    print target[2]
                    self.tts.say("J'ai détecté "+faceExtraInfo[2])
                else:
                    self.got_face = False


    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting HumanGreeter"
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping HumanGreeter"
            self.face_detection.unsubscribe("HumanGreeter")
            #stop
            sys.exit(0)



