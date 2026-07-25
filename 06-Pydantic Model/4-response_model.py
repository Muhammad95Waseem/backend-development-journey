from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from pydantic import BaseModel, Field

# Pydantic Schema enforcing automatic type validation
#================================================================
class Shipment(BaseModel):
    Product: str = Field(
        description="Product Title"
    )
    Status: str = Field(
        description="Tracking Status of the Order"
    )
    Amount: int = Field(
        description="Number of Items",
        gt=0, 
        le=100
        )
    Weight: int | float | None = Field(
        description="Weight of the Box",
        default=None
        )
#================================================================

db = {
    1101: {"Product": "Asus laptop", "Status": "Shipped", "Amount": 1, "Weight": 1},
    1102: {"Product": "Samsung S26", "Status": "Shipped", "Amount": 5, "Weight": 1.5},
    1103: {"Product": "HP laptop", "Status": "Delivered", "Amount": 3, "Weight": 2},
    1104: {"Product": "Smart Watch", "Status": "Pending", "Amount": 10, "Weight": 0.5}
}

app = FastAPI()

# Create a new shipment using QUERY PARAMETERS
@app.post("/add_shipment")
def add_shipment(id: int, data: Shipment):
    db[id] = {
        "Product": data.Product,
        "Status": data.Status,
        "Amount": data.Amount,
        "Weight": data.Weight
    }
    return "Success"

# Retrieve a single shipment by its integer ID via Query Parameter
@app.get("/get_shipment") 
def get_shipment(id: int) -> Shipment: # This allows to see details of the return body in docs
    order = db[id]
    return Shipment(
        Product=order['Product'],
        Status=order['Status'],
        Amount=order['Amount'],
        Weight=order['Weight']
    ) 

# Scalar API Documentation
@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scaler API"
    )

# To run the server: uvicorn "06-Pydantic Model.4-response_model:app" --reload