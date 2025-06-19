from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.controllers import post_category_controller
from app.schemas.post_category_schema import PostCategoryCreate, PostCategoryUpdate, PostCategoryOut

router = APIRouter(prefix="/categories", tags=["Post Categories"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[PostCategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return post_category_controller.read_categories(db)

@router.get("/{category_id}", response_model=PostCategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = post_category_controller.read_category(category_id, db)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=PostCategoryOut)
def create_category(category: PostCategoryCreate, db: Session = Depends(get_db)):
    return post_category_controller.create_category(category, db)

@router.put("/{category_id}", response_model=PostCategoryOut)
def update_category(category_id: int, category_data: PostCategoryUpdate, db: Session = Depends(get_db)):
    updated = post_category_controller.update_category(category_id, category_data, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    deleted = post_category_controller.delete_category(category_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted"}
