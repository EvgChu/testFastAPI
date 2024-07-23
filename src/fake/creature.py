from src.model.creature import Creature

_creatures = [
    Creature(
        name="Goblin",
        aka="aka Goblin",
        country="CN",
        area="Himalayes",
        description="Goblin is a very dangerous creature.",
    ),
    Creature(
        name="Bigfoot",
        aka="aka Bigfoot",
        country="US",
        area="*",
        description="Bigfoot is a very dangerous creature.",
    )
]

def get_all() -> list[Creature]:
    return _creatures

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(Creature: Creature) -> Creature:
    return Creature

def modify(Creature: Creature) -> Creature:
    return Creature

def replace(Creature: Creature) -> Creature:
    return Creature

def delete(name: str) -> bool:
    return False


