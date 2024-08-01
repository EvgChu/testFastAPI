from fastapi import FastAPI
from src.web import explorer
from src.web import creature

app = FastAPI(
    version="0.0.1",
)

app.include_router(explorer.router, tags=["Explorer"])
app.include_router(creature.router, tags=["Creature"])

@app.get("/echo/{thing}")
def echo(thing):
    return {"message": f"echo: {thing}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        forwarded_allow_ips="*",
    )
