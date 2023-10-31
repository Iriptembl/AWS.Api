from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def hello():
    return {"message": "Fast api for AWS"}