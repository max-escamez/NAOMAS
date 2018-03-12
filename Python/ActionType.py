from enum import Enum

# TODO : enum ne fonctionne pas avec python 2.7, trouver une nouvelle manière de programmer cette classe
class ActionType(Enum):
    MOVETO = 1
    TAKE = 2
    DROP = 3