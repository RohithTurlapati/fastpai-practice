import fake.explorer as data
from models.explorer import Explorer


def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get(name=name)

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer=explorer)

def modify(explorer: Explorer) -> Explorer:
    return data.modify(explorer=explorer)

def replace(explorer: Explorer) -> Explorer:
    return data.replace(explorer=explorer)

def delete(name: str) -> bool:
    return data.delete(name=name)