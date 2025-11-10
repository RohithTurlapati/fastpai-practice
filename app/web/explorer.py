from models.explorer import Explorer
from fastapi import APIRouter
import service.explorer as service


router = APIRouter(prefix="/explorer")


@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_explorer(name: str) -> Explorer | None:
    return service.get_one(name=name)