from src.model.explorer import Explorer
import src.data.explorer as data


def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get_one(name)

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)

def modify(name, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)

def replace(name, explorer: Explorer) -> Explorer:
    return data.replace(name, explorer)

def delete(name: str) -> bool:
    return False
