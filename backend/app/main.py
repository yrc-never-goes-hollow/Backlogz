from fastapi import FastAPI

app = FastAPI(title="Game Backlog API")


@app.get("/health")
def health():
    return {"status": "ok"}