#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Mains"""
import time
import sys
import numpy as np
from itertools import chain


class Search(object):

    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(Search, self).__init__()
        app.start()
        session = app.session
        # Get the services
        self.memory = session.service("ALMemory")
        self.tracker = session.service("ALTracker")
        self.motion = session.service("ALMotion")
        self.posture = session.service("ALRobotPosture")
        self.face_detection = session.service("ALFaceDetection")
        self.tts = session.service("ALTextToSpeech")
        self.auto = session.service("ALAutonomousLife")
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("FaceDetected")
        self.subscriber.signal.connect(self.on_human_tracked)
        self.face_detection.subscribe("Search")
        # Initiate variables
        self.got_face = False
        self.desires = {}
        self.believes = {}
        self.friends_list = []
        self.done = False
        # self.auto.setAutonomousAbilityEnabled('All', True)

    def on_human_tracked(self, value):
        """
        Callback for event FaceDetected.
        """
        self.face_detection.unsubscribe("Search")
        target_name = "Face"
        face_width = 0.1
        offset = 0.15
        self.tracker.registerTarget(target_name, face_width)
        if not value:  # empty value when the face disappears
            self.got_face = False
        elif not self.got_face:  # only speak the first time a face appears
            face_info_array = value[1]
            for j in range(len(face_info_array)-1):
                face_info = face_info_array[j]
                face_extra_info = face_info[1]
                if face_extra_info[2] in self.desires.keys() or face_extra_info[2] in self.friends_list:

                    self.got_face = True
                    self.tracker.track("Face")
                    target = self.tracker.getTargetPosition()
                    print target[0]
                    print target[1]
                    print target[2]
                    self.tts.say(face_extra_info[2]+", j'ai quelque chose à te dire !")
                    # phi = np.arctan2(target[1], target[0])
                    self.posture.goToPosture("Stand", 1.0)
                    if target[0]-offset > 0:
                        self.motion.moveTo(target[0]-offset, target[1], 0)
                    if face_extra_info[2] in self.desires.keys():
                        self.tts.say(self.desires[face_extra_info[2]][0])
                    else:
                        for key in self.believes.keys():
                            if face_extra_info[2] in self.believes[key]:
                                self.tts.say(self.desires[key][1])
                    # self.posture.goToPosture("Crouch", 1.0)
                    # self.face_detection.unsubscribe("Search")
                    self.done = True

                else:

                    self.got_face = False
                    self.face_detection.subscribe("Search")

    def run(self, desires,believes):
        """
        Loop on, wait for events until manual interruption.
        """
        self.desires = desires
        self.believes = believes
        self.friends_list = list(chain(*self.believes.values()))

        try:
            while not self.done:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user"
            self.face_detection.unsubscribe("Search")
            sys.exit(0)



