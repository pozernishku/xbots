import os
from enum import Enum


# Admin role
class Admin(Enum):
    ADMIN = int(os.environ["ADMIN"])
