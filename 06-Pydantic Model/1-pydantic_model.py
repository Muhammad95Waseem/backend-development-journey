from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from pydantic import BaseModel

# Pydantic Schema enforcing automatic type validation
#================================================================
class Shipment(BaseModel):
    Product: str
    Status: str
    Amount: int 
#================================================================

db = {
    1101: {"Product": "laptop", "Status": "Shipped", "Amount": 1},
    1102: {"Product": "Phone", "Status": "Shipped", "Amount": 5},
    1103: {"Product": "laptop", "Status": "Delivered", "Amount": 3},
    1104: {"Product": "Smart Watch", "Status": "Pending", "Amount": 10}
}

app = FastAPI()

@app.post("/add_shipment")
def add_shipment(id: int, data: Shipment):
    db[id] = {
        "Product": data.Product,
        "Status": data.Status,
        "Amount": data.Amount
    }
    return "Success"

# Retrieve a single shipment by its integer ID via query parameter
@app.get("/get_shipment")
def get_shipment(id: int):
    return db[id]

# Scalar API Documentation 
@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scaler API"
    )

# To run this server: uvicorn "06-Pydantic Model.1-pydantic_model:app" --reload