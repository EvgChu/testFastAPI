from fastapi import FastAPI
from src.web import explorer

app = FastAPI()

app.include_router(explorer.router)

@app.get("/echo/{thing}")
def echo(thing):
    return {"message": f"echo: {thing}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
