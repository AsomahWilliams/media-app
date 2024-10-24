from fastapi import FastAPI
from database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Media App",
    description = "Engine Behind Media App",
    version="0.1",
)