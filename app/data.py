from app.models import Creature


_creatures: list[Creature] = [
    Creature(name="rohith",
             country="india",
             area="hastinapuram",
             description="mad love with coding",
             aka="psychopragrammer"),
    
    Creature(name="gokul",
             country="india",
             area="mayurvihar",
             description="mad love with networking",
             aka="ratna"),
    
    Creature(name="koushik",
             country="india",
             area="vijayawada",
             description="mad love with business",
             aka="scardycat")
]

def get_creatures() -> list[Creature]:
    return _creatures
