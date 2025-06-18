from sqlalchemy.orm import Session
from app.models import PostCategory
from app.schemas.post_category_schema import PostCategoryCreate, PostCategoryUpdate

def read_categories(db: Session):
    return db.query(PostCategory).all()

def read_category(category_id: int, db: Session):
    return db.query(PostCategory).filter(PostCategory.id == category_id).first()

def create_category(category_data: PostCategoryCreate, db: Session):
    new_category = PostCategory(name=category_data.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def update_category(category_id: int, category_data: PostCategoryUpdate, db: Session):
    category = db.query(PostCategory).filter(PostCategory.id == category_id).first()
    if not category:
        return None
    category.name = category_data.name
    db.commit()
    db.refresh(category)
    return category

def delete_category(category_id: int, db: Session):
    category = db.query(PostCategory).filter(PostCategory.id == category_id).first()
    if not category:
        return False
    db.delete(category)
    db.commit()
    return True
