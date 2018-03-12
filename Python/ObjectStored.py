class ObjectStored:
    """ Class who define an object stored in the robot memory.
    The object is caracterized by :
    - its shape
    - its color
    - its position on x axis
    - its position on y axis
    """
        
    SHAPES_VALS = {'cube': 1, 'sphere': 2, 'pyramid': 3}
    COLORS_VALS = {'blue': 1, 'red': 2, 'green':3}
    ENERGY_COST = 1

    def __init__(self, f, c, x, y):
        """Constructor"""
        self.shape = f
        self.color = c
        self.x = x
        self.y = y
    
    def reward(object):
        """Calculate the reward"""
        return ObjectStored.SHAPES_VALS[object.shape] + ObjectStored.COLORS_VALS[object.color]
    
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
