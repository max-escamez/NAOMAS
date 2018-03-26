class BDI:
    """ mental representation of the robot
    attributs :
    - float x: position x
    - float y: position y
    - float r: rotation
    - dict believes: its believes
    - Desire desire
    """

    
    def __init__(self, desire):
        self.x = 0
        self.y = 0
        self.r = 0
        self.believes = {}
        self.desire = desire
    
    def add_face(self, face):
        pass
        #self.believes.append(face)
    
