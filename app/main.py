from fastapi import FastAPI

app = FastAPI()

@app.post("/tibber-developer-test/enter-path/")
async def move_robot():
    return {"test": "Hello World!"}
