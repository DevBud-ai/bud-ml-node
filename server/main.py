from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8080, reload=True)