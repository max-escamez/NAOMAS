import argparse
from naoqi import ALProxy


class Listen(object):
    """
    A simple class to react to a speech event.
    """

    def __init__(self, app, dictionnary):
        """
        Initialisation of naoqi framework and event detection.
        """
        super(Search, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("SpeechDetected")
        # ??????????????? self.subscriber.signal.connect(self.)
        # Get the services ALTextToSpeech and ALSpeechRecognition
        self.tts = session.service("ALTextToSpeech")
        self.asr = session.service("ALSpeechRecognition")
        # set the language of the speech recognition to French
        self.asr.setLanguage("French")
        self.asr.setVocabulary(dictionnary, True)
        # start the speech recognition
        self.asr.subscribe("SpeechRecognition")


    def on_human_speech(self, value):
        """
        Callback for event SpeechDetected.
        """
        pass


    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting speech recognition"
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping Speech recognition"
            self.asr.unsubscribe("SpeechRecognition")
            #stop
            sys.exit(0)