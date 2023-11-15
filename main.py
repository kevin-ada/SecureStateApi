from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import models
from database.db_conn import engine
from routers import posts, users, votes
from auth import login

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(votes.router)
models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def hello_world():
    return {"Status": "Valid"}
