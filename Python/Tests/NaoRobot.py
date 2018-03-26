from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from naoqi import ALMemory

class NaoRobot:
    """ main class of the naoRobot
    attributs :
    - float x: position x
    - float y: position y
    - float r: rotation
    - List<ObjectStored> believes: its believes
    - Desire desire
    - List<Action> intentions: its intentions
    - float gx, float gy : goal location
    - Action state: current action
    """
    
    NAO_IP = "127.0.0.1"
    PC_IP = "127.0.0.1"
    PORT = 9559
    
    def __init__(self, desire, goalx, goaly):
        self.x = 0
        self.y = 0
        self.r = 0
        self.believes = []
        self.desire = desire
        self.intentions = []
        self.gx = goalx
        self.gy = goaly
    
    def main():
        # Create a Local broker, connected to the remote naoqi
        broker = ALBroker("pythonBroker", PC_IP, 9999, NAO_IP, PORT)
        
        # subscribe to the object detection
        # Create a detection module
        estimationModule = EstimationModule(estimation_module)
        try:
            # Create a proxy to ALMemory
            memoryProxy = ALProxy("ALMemory", NAO_IP, PORT)
            # Suscribe to the event, saying where we want to be called
            memoryProxy.subscribeToEvent("PicturedDetected", "estimation_module", "estimate")
        
            # when a new picture is detected, shape an action plan
            # TODO : A CHAQUE PICTUREDETECTED
                # TODO : recupérer l'action faite par estimate dans EstimationModule et changer en conséquence les believes
                self.intentions = ActionPlan(self.believes, self.desire).actionPlan()
            # TODO : exécuter le plan d'action
            
        except RuntimeError, e:
        print e
        exit(1)
        
        