class Action
    """Class Action, define an action.
    attributs :
    - ActionType type : the type of the action
    - x, y = position of the object
    - object : if the robot cary an object
    """
    
    def __init__(self, type, x, y, object):
        """Constructor"""
        self.type = type
        self.x = x
        self.y = y
        self.object = object
    
    def equals(self, a):
        """Test of equality"""
        return (self.type == a.type and self.x == a.x and self.y == a.y)
