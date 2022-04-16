from typing import Optional
from fastapi import FastAPI, Request
from router import blog_get
from router import file
from router import blog_post
from router import user
from router import article
from router import product
from auth.authentication import router as authentication_router
from db.database import engine
from db import models
from exceptions import StoryException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(user.router)
app.include_router(file.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(authentication_router)


@app.get("/hello")
def index():
    return {"message": "Hello world!"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#   return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/files", StaticFiles(directory="files"), name="files")
