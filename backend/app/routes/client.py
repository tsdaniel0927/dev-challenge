import datetime as dt
from os import error, rename, path
from urllib.parse import urlencode
from typing import List
import requests
from fastapi import APIRouter, Depends  # Body,
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import config, models, utils, schemas
from pydantic import BaseModel


router = APIRouter()


@router.get("/clients", response_model=List[models.Client])
def get_clients(*, db: Session = Depends(utils.get_db)):
    clients = db.query(schemas.Client).all()
    return clients


@router.get("/client", response_model=models.Client)
def get_client(*, db: Session = Depends(utils.get_db), id:int):
    client = db.query(schemas.Client).filter(schemas.Client.id == id).first()
    return client


@router.post("/client", response_model=models.Client)
def create_client(
    *,
    db: Session = Depends(utils.get_db),
    client: models.Client
):
    client_data = client.dict(exclude_unset=True)
    db_client = schemas.Client(**client_data)
    db.add(db_client)
    db.commit()
    return db_client


@router.put("/client", response_model=models.Client)
def put_item(
    *,
    db: Session = Depends(utils.get_db),
    id: int,
    ## client:models.Client
):
    client_model = db.query(schemas.Client).filter(schemas.Client.id == id).first()

    client_model.update({ 'id':0, 'name':'bob', 'email':'bob@gmail.com', 'company':'BHP', 'address':'6000', 'age': 29}, synchronize_session=False)     ### error 422
    db.add(client_model)
    db.commit()
    
    return True


@router.delete("/client")
def delete_milestone_type_ref(
    *, db: Session = Depends(utils.get_db), id: int
):
    db.query(schemas.Client).filter(schemas.Client.id == id).delete()
    db.commit()



