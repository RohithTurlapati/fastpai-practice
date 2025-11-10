from app.models import Creature
from fastapi import FastAPI
from app.data import get_creatures


app = FastAPI()

@app.get("/creatures")
def get_all() -> list[Creature]:
    return get_creatures()