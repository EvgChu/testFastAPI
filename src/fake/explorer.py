from src.model.explorer import Explorer

_explorers = [
    Explorer(
        name="random",
        description="Random exploration",
        country="Ru",
    ),
    Explorer(
        name="greedy",
        description="Greedy exploration",
        country="Rn",
    ),
]

def get_all() -> list[Explorer]:
    return _explorers

def get_one(name: str) -> Explorer | None:
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
    return False
