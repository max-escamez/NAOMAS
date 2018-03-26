class ObjectStored:
    """ Class who define a face stored in the robot memory.
    The face is caracterized by :
    - its value
    - its position on x axis
    - its position on y axis
    """
        
    VALS = {'small': 1, 'medium': 2, 'big': 3}
    ENERGY_COST = 1

    def __init__(self, v, x, y):
        """Constructor"""
        self.value = v
        self.x = x
        self.y = y
    
    def reward(object):
        """Calculate the reward"""
        return ObjectStored.VALS[object.shape]
    
    def cost(object):
        """Calculate the movement energy cost"""
        """The movement from the object to the goal cost nothing"""
        return - ObjectStored.ENERGY_COST * (object.x + object.y)
        
    def total(object):
        """Calculate the reward less the cost"""
        return ObjectStored.reward(object) + ObjectStored.cost(object)
    
    def position(self, x0, y0):
        """Return the new position of the object"""
        self.x = self.x - x0
        self.y = self.y - y0
        return (self.x, self.y)
