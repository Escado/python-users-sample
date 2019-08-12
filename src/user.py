
from enum import Enum, auto

class Roles(Enum):
    Undefined = auto()
    Manager = auto()
    Administrator = auto()
    SoftwareDeveloper = auto()

class User():

    role = Roles.Undefined
    name = ''
    last_name = ''

    def __init__(self, role):
        self.role = role
    
    