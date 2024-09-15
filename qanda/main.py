from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/qanda")
async def say_hello(q: str = None):
    return {"message": f"Your question is {q}"}
