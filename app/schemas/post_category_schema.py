from pydantic import BaseModel

class PostCategoryBase(BaseModel):
    name: str

class PostCategoryCreate(PostCategoryBase):
    pass

class PostCategoryUpdate(PostCategoryBase):
    pass

class PostCategoryOut(PostCategoryBase):
    id: int

    class Config:
        orm_mode = True
