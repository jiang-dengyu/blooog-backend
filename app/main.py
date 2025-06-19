from fastapi import FastAPI
from app.routes import posts, post_categories

app = FastAPI()

# router
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(post_categories.router)