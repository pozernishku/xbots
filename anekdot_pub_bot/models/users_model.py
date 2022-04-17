import os
from enum import Enum

import dotenv

dotenv.load_dotenv()


# Admin role
class Admin(Enum):
    ADMIN = int(os.environ["ADMIN"])
