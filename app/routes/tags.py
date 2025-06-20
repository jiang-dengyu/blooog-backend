from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Session
from app.database import SessionLocal
#TODO: refractor contrller
#TODO: refractor Pydantic schema

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


@router.get('/')
def get_tags(db: Session = Depoends( get_db ))
tags = db.query(models.Tag).all()
return tags