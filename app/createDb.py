from app.db.model import Base
from app.db.session import engine

def create_db():
    Base.metadata.create_all(bind=engine)