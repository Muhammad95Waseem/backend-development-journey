from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

db = {
    1101: {"Product": "laptop", "Status": "Shipped"},
    1102: {"Product": "Phone", "Status": "Shipped"},
    1103: {"Product": "laptop", "Status": "Delivered"},
    1104: {"Product": "Smart Watch", "Status": "Pending"}
}

app = FastAPI()

# Updates an existing record in db
@app.put("/shipment/update")
def update(id: int, product: str, status: str):
    db[id] = {"Product": product, "Status": status}
    return db[id]

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

# To run this server: uvicorn "05-CRUD Operations.1-put_method:app" --reload
