from models.creature import Creature


_creatures: list[Creature] = [
    Creature(name="rohith",
             country="india",
             area="hastinapuram",
             description="creature",
             aka="psychopragrammer"),
    
    Creature(name="gokul",
             country="india",
             area="mayurvihar",
             description="creature",
             aka="ratna"),
    
    Creature(name="koushik",
             country="india",
             area="vijayawada",
             description="creature",
             aka="scardycat")
]

def get_all() -> list[Creature]:
    return _creatures

def get(name: str) -> Creature:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    return creature

def modify(creature: Creature) -> Creature:
    return creature

def replace(creature: Creature) -> Creature:
    return creature

def delete(name: str) -> bool:
    return None
