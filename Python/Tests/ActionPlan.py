class ActionPlan:
    """Shape the best action plan regarding to the believes and the desires.
    attributs :
    - believes : the believes
    - desire : the desire
    - actionPlan : the action plan
    """
    OPTIONS = {1 : ObjectStored.reward, 2 : ObjectStored.cost, 3 : ObjectStored.total}
    
    def __init__(self, shapes, d, action):
        """Constructor"""
        self.desire = d
        self.believes = {}
        for i in range(1,len(shapes) + 1):
            if (action.object.equals(shapes(i))):
                self.believes[shapes(i)] = ObjectStored.reward(shapes(i))
            else:
                self.believes[shapes(i)] = ActionPlan.OPTIONS[self.desire](shapes(i))
        self.actionPlan = []
        
    def actionPlan(self, goalx, goaly, action):
        """Shape the action Plan"""
        # find the object that maximise the cost
        object = max(value for key, value in self.believes.items())
        
        # action plan for this object : moveToward, takeIt, moveToGoal, dropIt
        self.actionPlan = [Action(ActionType.MOVETO, object.x, object.y), \
            Action(ActionType.TAKE, object.x, object.y) \
            Action(ActionType.MOVETO, goal.x, goal.y) \
            Action(ActionType.DROP, object. object.y) \
            ]
        return actionPlan
        
        