import uuid

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.util.UtilityFunction import transform, key

from app.db.session import get_db, get_redis

from app.db.model.Payload import Payload
from app.db.schema.Payload import PayloadInput, PayloadId, PayloadOutput


router = APIRouter(prefix="/payload", tags=["Payload"])

@router.post('/', status_code= HTTP_201_CREATED, response_model= PayloadId)
def create(cache_input : PayloadInput, cache = Depends(get_redis), db : Session = Depends(get_db)):
    cache_key = key(cache_input.list1,cache_input.list2)
    in_cache = cache.get(cache_key)
    if not in_cache:
        string_transform = transform(cache_input.list1,cache_input.list2)
        newPayload = Payload()
        newPayload.payload = string_transform
        db.add(newPayload)
        db.commit()
        in_cache = newPayload.id
        cache.set(cache_key, str(newPayload.id))
    return PayloadId(id = in_cache)

@router.get('/{id}', status_code= HTTP_200_OK, response_model= PayloadOutput)
def get(id: uuid.UUID, db : Session = Depends(get_db)):
    payload = db.query(Payload).filter(Payload.id == id).first()
    return payload