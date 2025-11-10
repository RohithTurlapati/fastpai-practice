import fake.creature as data
from models.creature import Creature


def get_all() -> list[Creature]:
    return data.get_all()

def get_one(name: str) -> Creature | None:
    return data.get(name=name)

def create(creature: Creature) -> Creature:
    return data.create(creature=creature)

def modify(creature: Creature) -> Creature:
    return data.modify(creature=creature)

def replace(creature: Creature) -> Creature:
    return data.replace(creature=creature)

def delete(name: str) -> bool:
    return data.delete(name=name)