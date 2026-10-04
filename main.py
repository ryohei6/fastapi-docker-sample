from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World from Dockerized FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
