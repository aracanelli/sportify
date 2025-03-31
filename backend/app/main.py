from fastapi import FastAPI
from app.api import auth

app = FastAPI()
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Spond clone backend is live!"}
