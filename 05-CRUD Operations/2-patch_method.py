from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

db = {
    1101: {"Product": "laptop", "Status": "Shipped"},
    1102: {"Product": "Phone", "Status": "Shipped"},
    1103: {"Product": "laptop", "Status": "Delivered"},
    1104: {"Product": "Smart Watch", "Status": "Pending"}
}

app = FastAPI()

# PATCH via Query Parameters (Manual Assignment)
# But if you have a large number of fields it will become hard to implement
@app.patch("/shipment/update")
def update(
    id: int, 
    product: str | None = None, 
    status: str | None = None
    ):

    shipment = db[id]
    if product:
        shipment["Product"] = product
    if status:
        shipment["Status"] = status
    db[id] = shipment

    return {"Detials": "Update Successful"}

# PATCH via Request Body (Dynamic Dictionary Update)
# Scales effortlessly with massive datasets and complex schemas.
@app.patch("/shipment/body_update")
def body_update(id: int, data: dict["str", "str"]):
    db[id].update(data)
    return {"Detials": "Update Successful"}

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

# To run this server: uvicorn "05-CRUD Operations.2-patch_method:app" --reload