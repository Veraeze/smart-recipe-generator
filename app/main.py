from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import recipes
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
app.include_router(recipes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Recipe Generator"}