from fastapi import FastAPI

app = FastAPI()

# Basic GET Request (Fetch data)
@app.get("/")
def root():
    return {"server status": "Active"}

# Command to run this server: uvicorn "02-FastAPI Basic.1-fastapi_endpoint:app" --reload