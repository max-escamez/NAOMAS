import time

from naoqi import ALModule

class EstimationModule(ALModule) :
    """analyse and store the new face in BDI"""

    def estimate(self, strVarName, value, strMessage):
        """callbak when data change"""
        
        print "datachanged", strVarName, " ", value, " ", strMessage
        # TODO : find a way to add the new object to the naoRobot believes