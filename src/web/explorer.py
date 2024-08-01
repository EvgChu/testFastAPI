from fastapi import APIRouter, HTTPException
from src.model.explorer import Explorer
import src.service.explorer as service
from src.errors import Missing, Duplicate

router = APIRouter(prefix="/explorer")

@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.message)

@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.message)

@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    try:
        return service.modify(explorer.name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.message)

@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer.name, explorer)

@router.delete("/{name}")
def delete(name: str) -> None:
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.message)
