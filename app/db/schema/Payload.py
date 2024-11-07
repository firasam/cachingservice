import uuid
from typing import List

from pydantic import BaseModel

class PayloadInput(BaseModel):
    list1 : List[str]
    list2 : List[str]

class PayloadOutput(BaseModel):
    id : uuid.UUID
    payload : str

class PayloadId(BaseModel):
    id : uuid.UUID