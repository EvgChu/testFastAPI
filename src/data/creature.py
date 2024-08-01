from src.data.init import (conn, cursor, IntegrityError)
from src.model.creature import Creature
from src.errors import Missing, Duplicate


cursor.execute(
    """CREATE TABLE IF NOT EXISTS creature (
        name TEXT PRIMARY KEY,
        country TEXT,
        description TEXT,
        area TEXT,
        aka TEXT
    )
    """
)


def row_to_model(row: tuple) -> Creature:
    return Creature(
        name=row[0],
        country=row[1],
        description=row[2],
        area=row[3],
        aka=row[4],
    )


def model_to_dict(model: Creature) -> dict:
    return model.to_dict()


def get_one(name: str) -> Creature:
    qry = "SELECT * FROM creature WHERE name=:name"
    params = {"name": name}
    cursor.execute(qry, params)
    row = cursor.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"Creature {name} not found")
    
    
def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature"
    cursor.execute(qry)
    return [row_to_model(row) for row in cursor.fetchall()]


def create(creature: Creature) -> Creature:
    if not creature: 
        return None
    qry = "INSERT INTO creature (name, country, description) VALUES (:name, :country, :description, :area, :aka)"
    params = model_to_dict(creature)
    try:
        cursor.execute(qry, params)
    except IntegrityError:
        raise Duplicate(f"creature {creature.name} already exists")
    
    return get_one(creature.name)


def modify(name: str, creature: Creature) -> Creature:
    if not creature: return None
    qry = """UPDATE creature 
            SET name=:name, 
                country=:country, 
                description=:description,
                area=:area,
                aka=:aka
            WHERE name=:name_orig"""
    params = model_to_dict(creature)
    params["name_orig"] = name
    cursor.execute(qry, params)
    if cursor.rowcount == 1: 
        return get_one(creature.name)
    else:
        raise Missing(f"creature {name} not found")
    
    
def replace(name: str, creature: Creature) -> Creature:
    return creature


def delete(name: str):
    if not name: return
    qry = "DELETE FROM creature WHERE name=:name"
    params = {"name": name}
    cursor.execute(qry, params)
    if cursor.rowcount != 1:
        raise Missing(f"creature {name} not found")
