from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scaler API"
    )

# To Run this Server: uvicorn "02-FastAPI Basics.2-documentation:app" --reload

# Past is browser: http://127.0.0.1:8000/scalar