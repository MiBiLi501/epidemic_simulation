import enum
from settings import *
from random import random
import numpy

class Status(enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2

class Agent():
    def __init__(self, x:float|None = None, y:float|None = None) -> None:
        self.status:int = Status.SUSCEPTIBLE
        self.x:float = random()*WIDTH if x == None else x
        self.y:float = random()*HEIGHT if y == None else y