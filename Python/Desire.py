from enum import Enum

# TODO : enum ne fonctionne pas avec python 2.7, trouver une nouvelle manière de programmer cette classe
class Desire(Enum):
    MAX_REWARD = 1
    MIN_COST = 2
    MAX_TOTAL = 3
    