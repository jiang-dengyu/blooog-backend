from app.database import SessionLocal
from app.models import Tag, PostCategory

def seed_tags_and_categories():
    db = SessionLocal()

    # 1. 假資料
    categories = ["backend","frontend"]
    tags = ["Javascript", "Laravel", "Python", "Docker", "FastAPI", "MySQL", "PostgreSQL", "domain knwoledge", "React"]

    # 2. 建立分類（避免重複）
    for name in categories:
        if not db.query(PostCategory).filter_by(name=name).first():
            db.add(PostCategory(name=name))

    # 3. 建立標籤
    for name in tags:
        if not db.query(Tag).filter_by(name=name).first():
            db.add(Tag(name=name))

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_tags_and_categories()