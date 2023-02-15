from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    msg = {
        "Message": "Hello, welcome to my FastAPI."
    }

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, log_level="info", reload=True)