from app import schemas
from .base import Base
from typing import List


class Client(Base):
    id : int = None
    name : str = None
    email : str = None
    company : str = None
    address : str = None



