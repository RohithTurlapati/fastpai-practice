from models.explorer import Explorer


_explorers: list[Explorer] = [
    Explorer(name="naveen",
             country="india",
             description="explorer"
             ),
    
    Explorer(name="golu",
             country="india",
             description="explorer"
            ),
    
    Explorer(name="ravi",
             country="india",
             description="explorer"
            )
]

def get_all() -> list[Explorer]:
    return _explorers

def get(name: str) -> Explorer:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None
        
def create(explorer: Explorer) -> Explorer:
    return explorer

def modify(explorer: Explorer) -> Explorer:
    return explorer

def replace(explorer: Explorer) -> Explorer:
    return explorer

def delete(name: str) -> bool:
    return None
