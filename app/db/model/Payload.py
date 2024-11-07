import uuid
from sqlalchemy import Column, String, UUID
from . import Base


class Payload(Base):
    __tablename__ = 'payloads'

    id = Column(UUID(as_uuid=True), primary_key= True, default = uuid.uuid4)
    payload = Column(String)