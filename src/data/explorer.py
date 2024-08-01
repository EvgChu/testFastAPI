from src.data.init import (conn, cursor, IntegrityError)
from src.model.explorer import Explorer
from src.errors import Missing, Duplicate


cursor.execute(
    """CREATE TABLE IF NOT EXISTS explorer (
        name TEXT PRIMARY KEY,
        country TEXT,
        description TEXT
    )
    """
)


def row_to_model(row: tuple) -> Explorer:
    return Explorer(
        name=row[0],
        country=row[1],
        description=row[2],
    )


def model_to_dict(model: Explorer) -> dict:
    return model.dict()


def get_one(name: str) -> Explorer:
    qry = "SELECT * FROM explorer WHERE name=:name"
    params = {"name": name}
    cursor.execute(qry, params)
    row = cursor.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"Explorer {name} not found")
    
    
def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer"
    cursor.execute(qry)
    return [row_to_model(row) for row in cursor.fetchall()]


def create(explorer: Explorer) -> Explorer:
    if not explorer: 
        return None
    qry = "INSERT INTO explorer (name, country, description) VALUES (:name, :country, :description)"
    params = model_to_dict(explorer)
    try:
        cursor.execute(qry, params)
    except IntegrityError:
        raise Duplicate(f"Explorer {explorer.name} already exists")
    
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    if not explorer: return None
    qry = "UPDATE explorer SET name=:name, country=:country, description=:description WHERE name=:name_orig"
    params = model_to_dict(explorer)
    params["name_orig"] = name
    cursor.execute(qry, params)
    if cursor.rowcount == 1: 
        return get_one(explorer.name)
    else:
        raise Missing(f"Explorer {name} not found")
    
    
def replace(name: str, explorer: Explorer) -> Explorer:
    return explorer


def delete(name: str):
    if not name: return
    qry = "DELETE FROM explorer WHERE name=:name"
    params = {"name": name}
    cursor.execute(qry, params)
    if cursor.rowcount != 1:
        raise Missing(f"Explorer {name} not found")
