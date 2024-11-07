from fastapi import FastAPI

from app.createDb import create_db
from app.router import Payload

create_db()
app = FastAPI()


app.include_router(Payload.router)
