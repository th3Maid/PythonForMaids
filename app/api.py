from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def wellcome() -> dict:
    return {"message": "Hello World!"}
