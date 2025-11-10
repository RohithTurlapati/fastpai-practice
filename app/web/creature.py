from models.creature import Creature
from fastapi import APIRouter
import service.creature as service


router = APIRouter(prefix="/creature")

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_creature(name: str) -> Creature | None:
    return service.get_one(name=name)